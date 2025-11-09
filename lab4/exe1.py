class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        print(f"Аккаунт для пользователя {self.username} успешно создан.")

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль был успешно изменен.")

    def check_password(self, password_to_check):
        return self.__password == password_to_check

def menu():
    print("    Создание нового аккаунта    ")
    username = input("Введите имя пользователя: ")
    email = input("Введите вашу электронную почту: ")
    password = input("Придумайте пароль: ")
    my_account = UserAccount(username, email, password)
    
    while True:
        print("\nЧто вы хотите сделать?")
        print("1 - Проверить пароль")
        print("2 - Изменить пароль")
        print("3 - Выйти из программы")
        choice = input("Выберите действие (введите номер): ")
        if choice == '1':
            password_to_check = input("Введите текущий пароль для проверки: ")
            if my_account.check_password(password_to_check):
                print("Верно! Пароль совпадает.")
            else:
                print("Неверный пароль.")

        elif choice == '2':
            old_password = input("Введите старый пароль для подтверждения: ")
            if my_account.check_password(old_password):
                new_password = input("Введите новый пароль: ")
                my_account.set_password(new_password)
            else:
                print("Старый пароль неверный. Изменение отменено.")

        elif choice == '3':
            print(f"До свидания, {my_account.username}!")
            break 

        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")
menu()