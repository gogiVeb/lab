class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Авторы: {self.author}, Год издания: {self.year}"


book = Book("Компьютерные сети 6-е издание", "Эндрю Таненбаум, Дэвид Уэзеролл и Ник Фимстер", 2024)

print(book.get_info())