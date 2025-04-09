class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = '0'

    def borrow(self, id):
        if self.status == '0':
            self.status = id
            return True
        return False

    def return_book(self):
        if self.status != '0':
            self.status = '0'
            return True
        return False

    def get_details(self):
        out = f"\t{self.title} by {self.author} ({'Available' if self.status == '0' else 'Borrowed'})"
        print(out)

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.title] = book

    def borrow_book(self, title, id):
        if title in self.books and self.books[title].borrow(id):
            return True
        return False

    def return_book(self, title):
        if title in self.books and self.books[title].return_book():
            return True
        return False

    def show_books(self):
        for title in self.books:
            self.books[title].get_details()

def main():
    library = Library()
    while(True):
        inp = input('>> ').split()
        if inp[0] == 'ADD':
            book = Book(inp[1][1:-1], inp[2][1:-1])
            library.add_book(book)
            print(f"Added {book.title} by {book.author}")
        elif inp[0] == 'BORROW':
            if library.borrow_book(inp[1][1:-1], '1'):
                print(f"Borrowed {inp[1][1:-1]}")
            else:
                print("there is an error")
        elif inp[0] == 'SHOW':
            print("Library Books")
            library.show_books()
        elif inp[0] == 'RETURN':
            if library.return_book(inp[1][1:-1]):
                print(f"Returned the {inp[1][1:-1]}")
            else:
                print("there is an error")
        elif inp[0] == 'exit':
            break
        else:
            print("""choose bitween
    1.ADD \"book title\" \"book author\"
    2.BORROW \"book title\"
    3.RETURN \"book title\"
    4.SHOW
    5.exit\n""")

if __name__ == '__main__':
    main()