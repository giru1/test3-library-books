import json
import os

from .Book import Book
from .utils import Status


class Library:
    def __init__(self, filename='library.json') -> None:
        self.books: list = []
        self.filename = filename

    def load_books(self):
        """Загрузка книг из файла."""
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, self.filename)

        if not os.path.exists(file_path):
            # Если файл не существует, создаем пустой файл
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

        with open(file_path, 'r', encoding='utf-8') as file:
            self.books = [Book(**book) for book in json.load(file)]

    def save_books(self):
        """Сохранение книг в файл."""

        current_directory = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(current_directory, self.filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def find_book_by_id(self, id_book: int) -> Book | None:
        """
        Поиск книги по id.
        :param id_book
        :return: Book | None
        """
        for book in self.books:
            if book.id == id_book:
                return book
        return None

    def add_book(self, title, author, year) -> None:
        """
        Добавление книги в библиотеку
        :param title:
        :param author:
        :param year:
        :return:
        """
        # Загружаем существующие книги
        self.load_books()

        # Создаем новую книгу
        book = Book(title, author, year)
        book.id = max((book.id for book in self.books), default=0) + 1

        # Добавляем книгу в список
        self.books.append(book)

        # Сохраняем все книги в файл
        self.save_books()
        print(book.__dict__)

    def delete_book(self, id_book: int) -> None:
        """
        Удаление книги
        :param id_book:
        :return:
        """

        book_to_remove: Book | None = self.find_book_by_id(id_book)

        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f'Книга с id {id_book} успешно удалена.')
        else:
            print(f'Книга с таким {id_book} не найдена.')

    def get_book(self, query: str | int) -> [Book]:
        """
        Поиск книги по title, author или year.
        :param query:
        :return: List[Book]
        """
        result = [book for book in self.books if
                   query in book.title or query in book.author or query in str(book.year)]

        if not result:
            print(f'Книга с таким {query} не найдена.')

        return result

    def get_books(self) -> [Book]:
        """
        Получие книг по фильтру
        :return: None
        """

        if len(self.books) == 0:
            print('Пока не добавлено ни одной книги!')

        for book in self.books:
            print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}"
            )

    def change_status(self, book_id: int, status: Status) -> Book:
        """
        Изменение книги
        :param book_id:
        :param status:
        :return:
        """

        # Загружаем существующие книги
        self.load_books()

        book_to_id: Book | None = self.find_book_by_id(book_id)
        if book_to_id is not None:
            book_to_id.status = str(status)

        # Сохраняем все книги в файл
        self.save_books()

        print(book_to_id.__dict__)











