class Book:
    books_dict = {}

    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
        Book.books_dict[title] = {'author': author, 'status': status}

    def return_book(self):
        if Book.books_dict[self.title]['status'] == 'Borrowed':
            Book.books_dict[self.title]['status'] = 'Available'
            return f"Returned {self.title}"
        return f"{self.title} is already Available"

    def borrow(self):
        if Book.books_dict[self.title]['status'] == 'Available':
            Book.books_dict[self.title]['status'] = 'Borrowed'
            return f"Borrowed {self.title}"
        return f"{self.title} is already Borrowed"

    def get_details(self):
        return f"{self.title} by {self.author} ({self.status})"


class Library(Book):
    def __init__(self):
            self.books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = {'author': author, 'status': 'Available'}
            Book.books_dict[title] = {'author': author, 'status': 'Available'}
            return f"Added {title} by {author}"
        return f"{title} already exists in library"

    def borrow_book(self, title):
        if title in self.books and self.books[title]['status'] == 'Available':
            self.books[title]['status'] = 'Borrowed'
            Book.books_dict[title]['status'] = 'Borrowed'
            return f"Borrowed {title}"
        return f"{title} is not available for borrowing"

    def return_book(self, title):
        if title in self.books and self.books[title]['status'] == 'Borrowed':
            self.books[title]['status'] = 'Available'
            Book.books_dict[title]['status'] = 'Available'
            return f"Returned {title}"
        return f"{title} is already available or not in library"

    def show_books(self):
        if not self.books:
            return "Library is empty"
        book_list = "\n".join([f"{title} by {info['author']} ({info['status']})"
                              for title, info in self.books.items()])
        return f"Library Books\n{book_list}"


# Processing commands
def process_commands(commands):
    library = Library()
    results = []

    for command in commands:
        parts = command.split('"')  # Spliting by quotes first
        action = parts[0].strip()   # Geting the commands

        if action == "ADD":
            title = parts[1].strip()
            author = parts[3].strip()
            results.append(library.add_book(title, author))
        elif action == "BORROW":
            title = parts[1].strip()
            results.append(library.borrow_book(title))
        elif action == "RETURN":
            title = parts[1].strip()
            results.append(library.return_book(title))
        elif action == "SHOW":
            results.append(library.show_books())

    return "\n".join(results)

# Geting commands from user input
command_number = int(input('Enter number of commands: '))
commands = []
for _ in range(command_number):
    command = input()
    commands.append(command)


print(process_commands(commands))




