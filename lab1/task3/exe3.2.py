def mode_selection():
    while True:
        mode = input("Укажите режим использования:\n"
                     "read - чтение файла\n"
                     "add - добавление текста в файл\n").lower().strip()
        if mode == "read":
            reading_selection()
            break
        elif mode == "add":
            additional_to_file()
            break
        else:
            print("\nВы указали неверный режим.")

def reading_file(mode):
    with open("example.txt", "r", encoding="utf-8") as file:
        if mode == "all":
            print(file.read())
        elif mode == "line":
            for line in file:
                print(line)
        elif mode == "list":
            print(file.readlines())

def additional_to_file():
    with open("example.txt", "a", encoding="utf-8") as file:
        message = input("\nНапишите, что Вы хотите добавить в файл.\n")
        file.write(f"{message}\n")

def reading_selection():
    while True:
        choice = input("Введите режим чтения:\n"
                       "all - чтение целиком,\n"
                       "line - чтение по строкам,\n"
                       "list - вывод строк списком\n").lower().strip()
        if choice in ("all", "line", "list"):
            reading_file(choice)
            break
        else:
            print("\nВы указали неверный формат чтения.")


mode_selection()