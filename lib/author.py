from lib.contract import Contract
from lib.book import Book

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or name.strip() == "":
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())
