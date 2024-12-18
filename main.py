from library.Library import Library
from library.utils import Status


def main():
    library: Library = Library()
    library.load_books()
    while True:
        print(
            "\n1. Добавить книгу"
            "\n2. Удалить книгу"
            "\n3. Поиск книги"
            "\n4. Отобразить все книги"
            "\n5. Изменить статус книги"
            "\n6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            title: str = input("Введите название книги: ")
            author: str = input("Введите автора книги: ")
            year: str = input("Введите год издания: ")
            library.add_book(title, author, year)
        elif choice == '2':
            book_id: int = int(input("Введите id книги для удаления: "))
            library.delete_book(book_id)
        elif choice == '3':
            query: str = input("Введите название, автора или год для поиска: ")
            results = library.get_book(query)
            for book in results:
                print(
                    f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        elif choice == '4':

            library.get_books()
        elif choice == '5':
            book_id: int = int(input("Введите id книги для изменения статуса: "))
            state_book: int = int(input(f"Введите новый статус ('в наличии - 1' или 'выдана - 0'): "))
            new_status: Status = Status.IN_STOCK.value if state_book == 1 else Status.ISSUED.value
            library.change_status(book_id, new_status)
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
