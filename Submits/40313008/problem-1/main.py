
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
        self.books = []  # books list

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Borrowed {book.title}")
                else:
                    print(f"{book.title} is not available")
                return
        print(f"Book titled '{title}' not found in library")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Returned {book.title}")
                return
        print(f"Book titled '{title}' not found in library")

    def show_books(self):
        print("Library Books:")
        for book in self.books:
            print(book.get_details())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    library = Library()

    library.add_book(Book("The Little Prince", "Antoine de Saint-Exupery"))
    library.add_book(Book("Moby-Dick", "Herman Melville"))

    library.borrow_book("The Little Prince")
    library.show_books()

    library.return_book("The Little Prince")
    library.show_books()



