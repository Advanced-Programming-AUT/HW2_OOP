# Completed

class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

    def borrow(self):
        if self.status == 'Available':
            self.status = 'borrowed'
            print('Borrowed ' + self.title)
        elif self.status == 'borrowed':
            print(self.title + ' is already Borrowed')
            pass

    def return_book(self):
        self.status = 'not-borrowed'

    def get_details(self):
        print('  ' + self.title + ' by ' + self.author + f" ({self.status})")


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, title, author):
        self.books.append(Book(title, author, 'Available'))
        print("Added " + title + " by " + author)

    def borrow_book(self, book):
        book.borrow()
        for bk in self.books:
            if bk.title == book.title:
                bk.status = 'borrowed'

    def return_book(self, book):
        book.status = 'Available'
        self.books.append(book)

    def show_books(self):
        print('Library Books')
        for book in self.books:
            book.get_details()


def main():
    main_library = Library([])
    while True:
        cmd = input()
        cmd = cmd.split('"')
        command = cmd[0]
        if command == 'SHOW':
            main_library.show_books()
        if command == 'ADD ':
            title = cmd[1]
            author = cmd[3]
            book = Book(title.replace('"', ""), author.replace('"', ""), 'Available')
            main_library.add_book(book.title, book.author)
        if command == 'BORROW ':
            title = cmd[1]
            author = cmd[3]
            book = Book(title.replace('"', ""), author.replace('"', ""), 'Available')
            main_library.borrow_book(book)
        if command == 'RETURN ':
            title = cmd[1]
            author = cmd[3]
            book = Book(title.replace('"', ""), author.replace('"', ""), 'Available')
            main_library.return_book(book)


main()
