import unittest
from library.library.utils import Status
from library.library.Library import Library
from pathlib import Path


class TestLibrary(unittest.TestCase):

    def setUp(self):
        test_dir = Path(__file__).parent
        self.library = Library(test_dir / 'test_library.json')
        self.library.load_books()

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", "2023")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")
        self.assertEqual(self.library.books[0].author, "Test Author")
        self.assertEqual(self.library.books[0].year, "2023")

    def test_delete_book(self):
        self.library.add_book("Test Book", "Test Author", "2023")
        book_id = self.library.books[0].id
        self.library.delete_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book_by_id(self):
        self.library.add_book("Test Book", "Test Author", "2023")
        book_id = self.library.books[0].id
        found_book = self.library.find_book_by_id(book_id)
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.title, "Test Book")

    def test_get_book(self):
        self.library.add_book("Test Book", "Test Author", "2023")
        results = self.library.get_book("Test Book")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Test Book")

    def test_change_status(self):
        self.library.add_book("Test Book", "Test Author", "2023")
        book_id = self.library.books[0].id
        self.library.change_status(book_id, Status.ISSUED.value)
        self.assertEqual(self.library.books[0].status, Status.ISSUED.value)

    def test_get_books(self):
        self.library.add_book("Test Book 1", "Test Author 1", "2023")
        self.library.add_book("Test Book 2", "Test Author 2", "2024")
        self.assertEqual(len(self.library.books), 2)

    def tearDown(self):
        import os
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')


if __name__ == '__main__':
    unittest.main()
