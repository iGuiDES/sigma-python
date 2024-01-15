"""
    Виконавець: Олександр Яценко
    Homework V - Група вимог III

    Цей скрипт дозволяє формувати власну електронну бібліотеку, з можливістю
    додавання, пошуку, видалення та перегляну.

    Пакетні версії:
    pip - v23.3.1
"""


class HomeLibrary:
    def __init__(self):
        self.books = {}

    def add_book(self, book_number: int, book_info: str) -> None:
        if book_number in self.books:
            print(f"Книга під номером {book_number} вже існує.")
            return
        self.books[book_number] = book_info

    def remove_book(self, book_number: str) -> None:
        if book_number in self.books:
            del self.books[book_number]
        else:
            print(f"Книга під номером {book_number} не знайдена.")

    def find_books(self, **search_criteria: list) -> list:
        found_books = []
        for number, book in self.books.items():
            if all(
                    book[key] == value for key, value in search_criteria.items()
            ):
                found_books.append((number, book))
        return found_books

    def get_book_by_number(self, book_number: int) -> str:
        return self.books.get(book_number, "Книгу не знайдено.")

    def display_all_books(self):
        for number, book in self.books.items():
            print(f"Номер: {number}, Книга: {book}")



