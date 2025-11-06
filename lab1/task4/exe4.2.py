import my_module


num1 = float(input('Введите первое число '))
num2 = float(input('Введите второе число '))


def expression_selection():

    while True:
        expression = input("Выберите какое выражение хотите сделать:\n"
                     "sum - Найти сумму\n"
                     "subtraction - Найти разность\n").lower().strip()
        
        if expression == "sum":
            print(f' Сумма данных чисел = {my_module.sum(num1, num2)}')
            break
        elif expression == "subtraction":
            print(f' Разность данных чисел  = {my_module.subtraction(num1, num2)}')
            break
        else:
            print("\n Повторите выбор выражения которое хотите совершить.")
        
expression_selection()