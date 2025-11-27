from lib.author import Author
from lib.book import Book

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str) or date.strip() == "":
            raise Exception("date must be a non-empty string")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("royalties must be a positive number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
