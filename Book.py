from utils import Status


class Book:
    def __init__(self, title, author, year, status=None, id=None):
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: Status = status if status else Status.IN_STOCK.value
