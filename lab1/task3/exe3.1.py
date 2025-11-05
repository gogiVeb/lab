def reading_file(mode):
    with open("lab1\example.txt", "r", encoding="utf-8") as file:
        if mode == "all":
            print(file.read())
        elif mode == "line":
            for line in file:
                print(line)
        elif mode == "list":
            print(file.readlines())


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


reading_selection()