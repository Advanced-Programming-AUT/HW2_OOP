books = [] # list of all books

class Book:
    def __init__(self,title,author,status):
        self.__title = title
        self.__author = author
        self.__status = status
        books.append(self)
        
    def borrow(self):
        if self.__status == "Available":
            self.__status = "Borrowed"
            
    def return_book(self):
        self.__status = "Available"
        
    def get_details(self):
        return f"- {self.__title} by {self.__author} ({self.__status})"

    def get_title(self):
        return self.__title

class Library:
    def __init__(self):
        self.books_available = []
        
    def add_book(self, title, author):
        book = Book(title, author, "Available")
        self.books_available.append(book)
        print(f"Added {title} by {author}")
        
    def borrow_book(self, title):
        count = 1
        for book in self.books_available:
            if book.get_title() == title:
                book.borrow()
                self.books_available.remove(book)
                print(f"Borrowed {title}")
                count = 0
                break
        if count:
            print("The book not exist\n")
            
    def return_book(self,title):
        for book in books:
            if book.get_title() == title:
                book.return_book()
                self.books_available.append(book)
                print(f"Returned {title}") 
                
    def show_books(self):
        print("Library Books:")
        for book in books:
            print(book.get_details())

library = Library()
number_count = int(input())
for _ in range(number_count):
    order_list = input().split("'")
    
    if order_list[0] == "ADD ":
        library.add_book(order_list[1], order_list[3])
        
    if order_list[0] == "BORROW ":
        library.borrow_book(order_list[1])
        
    if order_list[0] == "SHOW":
        library.show_books()
        
    if order_list[0] == "RETURN ":
        library.return_book(order_list[1])
        