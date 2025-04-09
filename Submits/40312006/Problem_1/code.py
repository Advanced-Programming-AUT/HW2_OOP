class Book:
    def __init__(self, name: str, author: str) -> None:
        self.name = name
        self.author = author
        self.status = True

    def __eq__(self, value) -> bool:
        if isinstance(value, Book):
            return self.name == value.name
        return self.name == value

    def __repr__(self) -> str:
        return f"\"{self.name}\" by \"{self.author}\""

    def borrow(self) -> bool:
        res = self.status
        self.status = False
        return res

    def return_book(self) -> None:
        self.status = True

    def get_details(self) -> None:
        print(f"{self.name} by {self.author} ({'Available' if self.status else 'Borrowed'})")

class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        if book in self.books:
            print(f"{book} already exists")
            return

        self.books.append(book)
        print(f"Added {book}")

    def borrow_book(self, title: str) -> None:
        try:
            idx = self.books.index(title)
        except ValueError:
            print(f"\"{title}\" not found")
            return

        if self.books[idx].borrow():
            print(f"Borrowed \"{title}\"")
        else:
            print(f"\"{title}\" has already been borrowed")

    def return_book(self, title: str) -> None:
        try:
            idx = self.books.index(title)
        except ValueError:
            print(f"\"{title}\" not found")
            return

        self.books[idx].return_book()
        print(f"Returned \"{title}\"")

    def show_books(self) -> None:
        print("Library Books")
        for i in self.books:
            print("\t", end='')
            i.get_details()

lib = Library()

while True:
    inp = input()
    if not inp:
        break

    code, data = inp.split(maxsplit=1)
    match code:
        case "ADD":
            _, name, _, author, _ = data.split('"')
            lib.add_book(Book(name, author))
        case "BORROW":
            lib.borrow_book(data.strip('"'))
        case "RETURN":
            lib.return_book(data.strip('"'))
        case "SHOW":
            lib.show_books()
        case _:
            print("Invalid execution code")
