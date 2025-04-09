import sys, os

original_stdout = sys.stdout

os.remove('output.txt')

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'a')

sys.stdout = file2

# ---------- Main Code ----------

class Book:
    def __init__(self, title, author, status = 'Available'):
        self.__title = title
        self.__author = author
        self.__status = status

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def borrow(self):
        if self.__status == 'Available':
            self.__status = 'Borrowed'
            print(self.__status, self.__title)
        else:
            print(self.__title, 'is not Available')

    def return_book(self):
        if self.__status == 'Available':
            print(self.__title, 'has not been borrowed yet!')
        else:
            self.__status = 'Available'
            print('Returned', self.__title)

    def get_details(self):
        print(' ', self.__title, 'by', self.__author, f'({self.__status})')

class Library:
    def __init__(self):
        self.__books = dict()

    def add_book(self, book):
        if book.title in self.__books:
            print('This book exists in Library. But we will update it for you :)')

        self.__books[book.title] = book
        print('Added', book.title, 'by', book.author)

    def borrow_book(self, title):
        if title not in self.__books:
            print('This book does not exist!')
        else:
            self.__books[title].borrow()

    def return_book(self, title):
        if title not in self.__books:
            print('This book does not exist!')
        else:
            self.__books[title].return_book()

    def show_books(self):
        print('Library Books')
        for book in self.__books.values():
            book.get_details()

if __name__ == '__main__':
    library = Library()
    while 1:
        command = file1.readline().strip()
        command = [line.strip() for line in list(command.split('\"')) if line.strip()]

        if len(command) == 0:
            break

        if command[0] == 'ADD':
            library.add_book(Book(command[1], command[2]))
        elif command[0] == 'BORROW':
            library.borrow_book(command[1])
        elif command[0] == 'RETURN':
            library.return_book(command[1])
        elif command[0] == 'SHOW':
            library.show_books()
        else:
            print('WRONG command!!!')


# ---------- End of Main Code ----------

sys.stdout = original_stdout

file1.close()
file2.close()