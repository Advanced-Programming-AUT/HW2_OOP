class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def borrow(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return True
        return False

    def return_book(self):
        self.status = "Available"

    def get_details(self):
        return f"{self.title} by {self.author} ({self.status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.borrow():
                print(f"Borrowed {book.title}")
                return
        print(f"Book '{title}' is not available")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                print(f"Returned {book.title}")
                return
        print(f"Book '{title}' not found in library")

    def show_books(self):
        print("Library Books")
        for book in self.books:
            print(f"  {book.get_details()}")

def main():
    library = Library()

    while True:
        command = input().lower().split("\"")
        #print('+++')
        #print(command)
        if command[0] == "quit":
            break
        elif command[0] == "add ":
            library.add_book(Book(command[1], command[3]))
        elif command[0] == "borrow ":
            library.borrow_book(command[1])
        elif command[0] == "return ":
            library.return_book(command[1])
        elif command[0] == "show":
            library.show_books()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
