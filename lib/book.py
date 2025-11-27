class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or title.strip() == "":
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)
