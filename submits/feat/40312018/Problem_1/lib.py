class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"
    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return True
        return False

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return True
        return False

    def get_details(self):
        return f"{self.title} by {self.author} ({self.status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.borrow():
                    print(f"Borrowed {book.title}")
                return

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"Returned {book.title}")
                return

    def show_books(self):
        print("Library Books")
        for book in self.books:
            print(book.get_details())


def main():
    library = Library()
    while True:
        s = input()

        request = s.split()[0].upper()
        part = s.split('"')
        if request == "ADD":
            title = part[1]
            author = part[3]
            library.add_book(Book(title, author))
        elif request == "BORROW":
            title = part[1]
            library.borrow_book(title)
        elif request == "RETURN":
            title = part[1]
            library.return_book(title)
        elif request == "SHOW":
            library.show_books()


main()
