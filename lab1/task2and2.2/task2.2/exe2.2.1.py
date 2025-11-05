# 2.2.1 Работа с аргументами функций
# Напишите функцию describe_person, принимающую имя и возраст человека, и 
# печатающую эту информацию в читаемом виде. Сделайте возраст опциональным 
# аргументом со значением по умолчанию 30.

def describe_person(name, age=30):
  description = f'Имя: {name}, Возвраст: {age} лет'
  return description
user_name = input('Введите ваше Имя: ')
user_age = input('Введите ваш возраст или нажмите Enter (по умолчанию 30):  ')
if user_age.strip():
  info = describe_person(user_name, int(user_age))
else:
  info = describe_person(user_name)
print(" Информация о пользователе! ")
print(info)