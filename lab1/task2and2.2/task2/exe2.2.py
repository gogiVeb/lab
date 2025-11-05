# 2.2 Создайте функцию square, которая возвращает квадрат переданного ей числа
def square (num, n = 2):
    return num ** n
num_square = square(int(input('Введите число и получите его в квадрате!: ')))
print(num_square)