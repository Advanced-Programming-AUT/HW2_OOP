class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def get_details(self):
        return f"{self.title} by {self.author} ({self.status})"

    def return_book(self):
        self.status = "Available"

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return True
        return False

class Library(object):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.borrow():
                print(f"Borrowed {book.title}")
                return
        print(f"{title} is not available for borrowing.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.status == "Borrowed":
                book.return_book()
                print(f"Returned {book.title}")
                return
        print(f"{title} was not borrowed.")

    def show_books(self):
        print("Library Books")
        for book in self.books:
            print(f"  {book.get_details()}")

library = Library()
library.add_book(Book("The Little Prince", "Antoine de Saint-Exupéry"))
library.add_book(Book("Moby-Dick", "Herman Melville"))

library.borrow_book("The Little Prince")
library.show_books()
library.return_book("The Little Prince")
library.show_books()