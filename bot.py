import vk_api, asyncio
from vk_api.longpoll import VkLongPoll, VkEventType
from config import token_api
from duck_chat import DuckChat, ModelType

async def chat_with_model(user_input, role_description):
    """Отправляет пользовательский ввод и получает ответ от модели с учетом роли."""
    models = [ModelType.GPT4o]
    responses = []

    # Формируем текст запроса, добавляя описание роли
    prompt = f"Вы являетесь {role_description}. Ответьте на следующий вопрос: {user_input}"

    for model_type in models:
        async with DuckChat(model=model_type.value) as chat:
            response = await chat.ask_question(prompt)
            responses.append(response)

    return "\n".join(responses)

async def main():
    # Ваш токен
    token = token_api
    
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    
    role_description = (
        "горничная, которая должна обслуживать только клиентов"
        "только будут отвечать вопросы насчёт общение"
        "горничная, не должно имеет знание науки"
        "так же горничная, должна ответить только который связаны с работы горничная"
    )

    while True:  # Постоянно слушаем события
        for event in longpoll.listen():  # Используем обычный цикл for
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text
                peer_id = event.peer_id
                
                print(f'Получено сообщение от {peer_id}: {text}')
                
                response = await chat_with_model(text, role_description)  # Ожидание ответа

                vk.messages.send(
                    peer_id=peer_id,
                    message=response,
                    random_id=vk_api.utils.get_random_id()
                )

if __name__ == '__main__':
    asyncio.run(main())