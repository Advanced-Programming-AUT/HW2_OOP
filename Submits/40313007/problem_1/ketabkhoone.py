class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_books(self, title):
        for book in self.books:
            if book.title == title:
                if not book.status:
                    book.borrow()
                    print(f"You have borrowed '{book.title}' by {book.author}.")
                    return
                else:
                    print(f"'{book.title}' is currently borrowed.")
                    return
        print(f"'{title}' not found in the library.")

    def return_books(self, title):
        for book in self.books:
            if book.title == title:
                if book.status:
                    book.return_book()
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"'{title}' not found in the library.")

    def show_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            for book in self.books:
                book.get_details()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = False  # False means available, True means borrowed

    def borrow(self):
        if not self.status:  # If it's not borrowed
            self.status = True

    def return_book(self):
        if self.status:  # If it is borrowed
            self.status = False

    def get_details(self):
        print(f"{self.title} by {self.author}", end=' ')
        if self.status:
            print("(Borrowed)")
        else:
            print("(Available)")


# Using the classes
lib = Library()

n = int(input("Enter the number of commands: "))

for i in range(n):
    x = input()
    y = x.split(' "')
    if y[0] == "ADD":
        book = Book(y[1], y[2])
        lib.add_books(book)
    elif y[0] == "BORROW":
        lib.borrow_books(y[1])
    elif y[0] == "RETURN":
        lib.return_books(y[1])
    elif y[0] == "SHOW":
        lib.show_books()

