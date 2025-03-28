import shlex

class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.status = 'Avalable'
    
    def borrow(self):
        self.status = 'Borrowed'

    def return_book(self):
        self.status = 'Avalable'

    def get_details(self):
        return f'{self.title} by {self.author}'
    
class Library:
    
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        return f'Added {title} by {author}'
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.status == 'Avalable':
                book.borrow()
                return f'Borrowed {title}'
            else:
                return f'The book is unavalable'
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return f'Returned {book.title}'
            
    def show_books(self):
        output = 'Library books\n'
        for book in self.books:
            output += f'{book.title} by {book.author} ({book.status})\n'
        return output.strip()

def main():    
    l1 = Library()
    output = []
    while True:
        com = shlex.split(input())
        match com[0]:
            case 'ADD':
                output.append(l1.add_book(com[1], com[2]))
            case 'BORROW':
                output.append(l1.borrow_book(com[1]))
            case 'SHOW':
                output.append(l1.show_books())
            case 'RETURN':
                output.append(l1.return_book(com[1]))
            case 'END':
                break
            case _:
                print('invalid input')

    for out in output:
        print(out)

if __name__ == '__main__':
    main()