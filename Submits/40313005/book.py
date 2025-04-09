class Book:
    def __init__(self,title,author,status):
        self.title = title
        self.author = author
        self.status = status
        print(f"Added {self.title} by {self.author}")
    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"

    def return_book(self):
        self.status = "Available"

    def get_details(self):
        print(f"{self.title} by {self.author} ({self.status})")


class Library():
    def __init__(self):
        self.books_list = []


    def add_book(self,Book):
        self.books_list.append(Book)

    def borrow_book(self,title):
        for book in self.books_list:
            if book.title == title:
                book.borrow()

    def return_book(self,title):
        for book in self.books_list:
            if book.title == title:
                book.return_book()
    def show_books(self):
        for book in self.books_list:
            book.get_details()

library = Library()

while (True):
    command = input()
    splited_command = command.split("\"")
    print(splited_command)
    match splited_command[0].strip():
        case "q":
            break
        case "SHOW":
            library.show_books()
        case "BORROW":
            library.borrow_book(splited_command[1])
        case "ADD":
            new_book = Book(splited_command[1],splited_command[3],"Available")
            library.add_book(new_book)
        case "RETURN":
            library.return_book(splited_command[1])
