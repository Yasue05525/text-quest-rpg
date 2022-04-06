import random as r
import time

time.sleep(3)
print("Квестовая игра...")
time.sleep(3)
print("Началось...")
time.sleep(3)

name = input("Как вас зовут?: ")
age = input("Сколько тебе лет?: ")

time.sleep(3)
print("Привет,", name, "Я создатель этого проекта")
time.sleep(3)
print("Щас, вы начинаете путешествие")
time.sleep(3)
print("Ваша задача, использовать такие команды как (да/нет), потом начнут и другие команды")
time.sleep(3)
print("Вы готовы дети? (Да/Нет)..")

otv1 = input("Ваш ответ!: ")

while True:
	if otv1 == 'да':
		print("Так", name, "Начнем игру..")
		time.sleep(3)
		print(name, ": *Куда-то ушел*")
		time.sleep(3)
		print(name, "Сразу увидел лес и заблудился, что вы собираетесь сделать?")
		time.sleep(3)
		print("Выберите (Выживать) или (Убегать)")
		
		otv2 = input("Ваш ответ?: ")
		
		if otv2 == 'выживать':
			time.sleep(3)
			print(name, "Хороший выбор, а теперь приступим к выживание!")
			time.sleep(3)
			print("Вы нашли палку забрать или нет?")
			time.sleep(3)
			
			otv3 = input("Ваш ответ?: ")
			
			if otv3 == 'да':
				time.sleep(3)
				print("Молодец,", name, "Вы забрали палку!")
				time.sleep(3)
				print("А теперь будете забрать камень?")
				time.sleep(3)
				
				otv4 = input("Ваш ответ?: ")
				
				if otv4 == 'Да':
					time.sleep(3)
					print("Молодец,", name, "Вы забрали, камень")
					time.sleep(3)
					print("Вы будете крафтит меч или кирку?")
					time.sleep(3)
					break
				
				elif otv4 == 'нет':
					time.sleep(3)
					print("Как ты собирался убить врага, даже без камня, придется заново!")
					time.sleep(3)
				
				break
			
			elif otv3 == 'нет':
				time.sleep(3)
				print("Если будете без палки, ты не будеш безопасный, придется заново начать!")
				time.sleep(3)
				break
			
			break
			
		elif otv2 == 'убегать':
			time.sleep(3)
			print("А вот это зря, ты еше заблудился, придется заново!")
			break
		break
	elif otv1 == 'нет':
		print("Я вижу", name, "Еще не готов, мне придется остановить игру")
		break