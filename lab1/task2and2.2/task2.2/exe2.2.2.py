# 2.2.3 Использование функций для решения алгоритмических задач
# Напишите функцию is_prime, которая определяет, является ли число простым, и 
# возвращает True или False соответственно.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def checking_num(text):
    while True:
        number = input(text).strip()
        if number.isdigit():
            return int(number)
        print("Вводите только положительные числа.")
user_num = checking_num("Введите число: ")
print(is_prime(user_num))