# 2.3 Реализуйте функцию max_of_two, которая принимает два числа в качестве 
# аргументов и возвращает большее из них.
def max_of_two(x, y):
    if x != y:
        return f"\nБольшее число: {max(x, y)}"
    return "\nЧисла равны."


def error_checking(text):
    while True:
        number = input(text)
        try:
            return float(number)
        except ValueError:
            print("Вводите только числа.\n")

user_num1 = error_checking("Введите первое число: ")
print("")
user_num2 = error_checking("Введите второе число: ")
print(max_of_two(user_num1, user_num2))
