class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__status = "Available"

    def borrow(self):
        if self.__status == "Available":
            self.__status = "Borrowed"
            return f"Borrowed {self.__title}"
        return f"{self.__title} is already borrowed :( , try another one."

    def return_book(self):
        if self.__status == "Borrowed":
            self.__status = "Available"
            return f"Returned {self.__title}"
        return f"{self.__title}  is available , it was not borrowed "

    def get_details(self):
        return f"{self.get_title} by {self.__author} ({self.get_status})"

    def get_title(self):
        return self.__title

    def get_status(self):
        return self.__status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book2 = Book(title, author)
        self.books.append(book2)
        return f"Added {title} by {author}"

    def borrow_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book.borrow()
        return f"Book '{title}' not found,try again..."

    def return_book(self, title):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book.return_book()
        return f"Book '{title}' not found,try again..."

    def show_books(self):
        if not self.books:
            return "no books for you"
        result = "Library Books:\n"
        for book in self.books:
            result += "  " + book.get_details() + "\n"
        return result.strip()

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.get_title().lower():
                return book.get_details()
        return f"No books for you with title '{title}'"

    def show_borrowed_books(self):
        borrowed_books = [book.get_details() for book in self.books if book.get_status() == "Borrowed"]
        return "\n".join(borrowed_books) if borrowed_books else " there is No borrowed books"


library = Library()
while True:
    request = input("Enter  (ADD, BORROW, RETURN, SHOW, SEARCH, SHOW_BORROWED, EXIT): ").strip().upper()
    if request == "ADD":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        print(library.add_book(title, author))
    elif request == "BORROW":
        title = input("Enter book title: ").strip()
        print(library.borrow_book(title))
    elif request == "RETURN":
        title = input("Enter book title: ").strip()
        print(library.return_book(title))
    elif request == "SHOW":
        print(library.show_books())
    elif request == "SEARCH":
        title = input("Enter book title to search: ").strip()
        print(library.search_book(title))
    elif request == "SHOW_BORROWED":
        print(library.show_borrowed_books())
    elif request == "EXIT":
        break
    else:
        print(" try again...")


