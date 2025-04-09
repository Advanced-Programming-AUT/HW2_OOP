class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return f"{self.title} has been borrowed."
        return f"{self.title} is already borrowed."

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return f"{self.title} has been returned."
        return f"{self.title} wasn't borrowed."

    def get_details(self):
        return f"{self.title} by {self.author} is {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return f"Added book: {title} by {author}"

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title:
                return book.borrow()
        return f"Book '{title}' not found in the library."

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title:
                return book.return_book()
        return f"Book '{title}' not found in the library."

    def show_books(self):
        if not self.books:
            return "No books in the library."
        result = "Library Books:\n"
        for book in self.books:
            result += f"{book.get_details()}\n"
        return result


library = Library()
print(library.add_book("The Little Prince", "Antoine de Saint-Exupéry"))
print(library.add_book("Moby-Dick", "Herman Melville"))
print(library.borrow_book("The Little Prince"))
print(library.show_books())
print(library.return_book("The Little Prince"))
print(library.show_books())
