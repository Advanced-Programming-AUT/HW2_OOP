class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return True
        else:
            return False
    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return True
        else:
            return False
    def get_details(self):
        return f"{self.title} by {self.author} ({self.status})"
class Library(Book):
    def __init__(self):
        self.books = []
    def add_book(self, title, author):
        self.books.append(Book(title, author, "Available"))
        print(f"Added {title} by {author}")
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Borrowed {title}")
                else:
                    print(f"{title} is not available")
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned {title}")
    def show_books(self):
        print("Library Books")
        for book in self.books:
            print(f"\t{book.get_details()}")
library = Library()
while True:
    command = input().strip()
    command_list = list(command.split())
    info_list = command.split('"')
    if command_list[0] == "ADD":
        library.add_book(info_list[1], info_list[3])
    elif command_list[0] == "BORROW":
        library.borrow_book(info_list[1])
    elif command_list[0] == "RETURN":
        library.return_book(info_list[1])
    elif command_list[0] == "SHOW":
        library.show_books()
    else:
        print("invalid")
        break
