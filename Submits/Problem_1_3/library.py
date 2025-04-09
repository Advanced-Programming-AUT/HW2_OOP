class Books:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__status = "available"

    def borrow(self):
        if self.__status == "available":
            self.__status = "borrowed"
            return True
        return False

    def return_book(self):
        if self.__status == "borrowed":
            self.__status = "available"
            return True
        return False

    def get_details(self):
        return f"Title: {self.__title}, Author: {self.__author}, Status: {self.__status}"

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def status(self):
        return self.__status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"title": book.title, "author": book.author, "borrowed": False})
        print(f"Added {book.title} by {book.author}")

    def borrow_book(self, title):
        for book in self.books:
            if book["title"] == title:
                if not book["borrowed"]:
                    book["borrowed"] = True
                    print(f"Borrowed {title}")
                    return
                else:
                    print(f"{title} has alredy been borrowed")
                    return
                print(f"the {title} not available in library")

    def return_book(self, title):
        for book in self.books:
            if book["title"] == title:
                if book["borrowed"]:
                    book["borrowed"] = False
                    print(f"Returned {title}")
                    return
                else:
                    print(f"{title} was not borrowed")
                    return
                print(f"{title} not available in library")

    def show_books(self):
        if not self.books:
            print("library is empty")
        else:
            for book in self.books:
                status = "Borrowed" if book["borrowed"] else "available"
                print(f"{book["title"]} by {book["author"]} ({status})")

if __name__ == "__main__":
    library = Library()
    b1 = Books("the little prince", "Antoine de Saint-Exupéry")
    b2 = Books("Moby-Dick", "Herman Melville")

    library.add_book(b1)
    library.add_book(b2)

    library.borrow_book("the little prince")
    print("Library Books")
    library.show_books()

    library.return_book("the little prince")
    print("Library Books")
    library.show_books()