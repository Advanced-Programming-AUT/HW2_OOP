class Book:
    def __init__(self, title, author, status):
        self._title = title
        self._author = author
        self._status = status
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def status(self):
        return self._status
    def borrow(self):
        if self._status == 'Borrowed':
            raise ValueError('The book is borrowed')
        self._status = 'Borrowed'
        print(f'Borrowed {self._title}')
    def returnbook(self):
        self._status = 'Available'
        print(f'Returned {self._title}')
    def get_details(self):
        print(f'\t{self._title} by {self._author} ({self._status})')

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f'Added {book.title} by {book.author}')
    def borrow_book(self, title):
        for book in self.books:
            if title == book.title:
                book.borrow()
                return
        print(f'{title} is not found')
    def return_book(self, title):
        for book in self.books:
            if title == book.title:
                book.returnbook()
    def show_books(self):
        print('Library books')
        for book in self.books:
            book.get_details()

if __name__ == '__main__':
    library = Library()
    command = str
    while command != ' ':
        command = input()
        if 'ADD' in command:
            command = command.split('"')
            title = command[1]
            author = command[3]
            status = 'Available'
            book = Book(title, author, status)
            library.add_book(book)
        elif 'BORROW' in command:
            command = command.split('"')
            title = command[1]
            library.borrow_book(title)
        elif 'RETURN' in command:
            command = command.split('"')
            title = command[1]
            library.return_book(title)
        elif 'SHOW' in command:
            library.show_books()
