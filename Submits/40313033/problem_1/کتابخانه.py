class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return f"Borrowed {self.title}"
        else:
            return f"{self.title} is already borrowed"

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return f"Returned {self.title}"
        else:
            return f"{self.title} was not borrowed"

    def get_details(self):
        return f"  {self.title} by {self.author} ({self.status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return f"Added {title} by {author}"

    def show_books(self):
        if not self.books:
            return "Library is empty"
        result = ["Library Books"]
        for book in self.books:
            result.append(book.get_details())
        return "\n".join(result)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return f"{title} was not found in the library"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return f"{title} was not found in the library"


library = Library()

while True:
    try:
        command = input().strip()
        if not command:
            continue

        parts = command.split(" ", 1)
        action = parts[0]

        if action == "ADD":
            title_author = parts[1].split('" "')
            author = title_author[1].replace('"', '')
            title = title_author[0].replace('"', '')
            print(library.add_book(title, author))

        elif action == "BORROW":
            title = parts[1].replace('"', '')
            print(library.borrow_book(title))

        elif action == "RETURN":
            title = parts[1].replace('"', '')
            print(library.return_book(title))

        elif action == "SHOW":
            print(library.show_books())

        else:
            print("Invalid command")

    except EOFError:
        break
