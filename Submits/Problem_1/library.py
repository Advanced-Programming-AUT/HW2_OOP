class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def borrow(self):
        self.status = 'Borrowed'

    def return_book(self):
        self.status = 'Available'

    def get_details(self):
        print(f"    {self.title} by {self.author} ({self.status})")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.status == 'Available':
                book.borrow()
                print(f"Borrowed {book.title}")
                return True
        return False

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title and book.status == 'Borrowed':
                book.return_book()
                print(f"Returned {book.title}")
                return True
        return False

    def show_books(self):
        print("Library Books")
        for book in self.books:
            book.get_details()


def main():
    library = Library()
    command = input().split('"')
    while command[0] != 'EXIT':
        match command[0]:
            case 'ADD ':
                title = command[1]
                author = command[3]
                book = Book(title, author, "Available")
                library.add_book(book)
            case 'BORROW ':
                title = command[1]
                status = library.borrow_book(title)
                if not status:
                    print("Book is not available")
            case 'RETURN ':
                title = command[1]
                status = library.return_book(title)
                if not status:
                    print("Book is already returned")
            case 'SHOW':
                library.show_books()
        command = input().split('"')


if __name__ == '__main__':
    main()

'''
ADD "the little prince" "Antoine de Saint-Exupéry"
ADD "Moby-Dick" "Herman Melville"
BORROW "the little prince"
SHOW
RETURN "the little prince"
SHOW

'''
