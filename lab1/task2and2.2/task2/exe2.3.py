# 2.3 Реализуйте функцию max_of_two, которая принимает два числа в качестве 
# аргументов и возвращает большее из них.
def max_of_two (num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2 
    else:
        return num1
num1 = int(input('Введите первое число !: '))
num2 = int(input('Введите второе число !: '))
result = max_of_two(num1, num2)
if result is num1:
    print(f'Числа {num1} и {num2} равны ! ')
else:
    print(f'Число {result} больше ! ')
