import int_module
import str_module

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Сумма: ",int_module.sum(num1, num2))
print("Разница ",int_module.sub(num1, num2))
print("Умножение ",int_module.mul(num1, num2))

name = input("Как тебя зовут? ")
word = input("Напишите любое слово: ")

print(str_module.greet(name))
print("Верхний регистр",str_module.big_str(word))

    