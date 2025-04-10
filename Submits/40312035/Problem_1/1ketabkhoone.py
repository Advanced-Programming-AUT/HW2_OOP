class Book:
    def init(self , title , author   ):
        self.__title = title
        self.__author = author
        self.__status = 'available'

    def borrow(self):
        if self.__status == 'available':
            self.__status = 'not available' ; print('amanat dade shod')
        else:
            print('not available')

    def return_book( self):
        self.__status = 'available' ; print('done')




    def get_details( self):
        return {
            'title': self.__title,
            'author': self.__author,
            'status': self.__status
        }

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__status





class Library:
    def init(self):
        self.__books =[]
    def add_book(self , book):
        self.__books.append(book)
        print('added')
    def borrow_book(self , title):
        for book in self.__books:
            if title ==book.get_title():
                book.borrow() ; return
    def return_book(self , title):
        for book in self.__books:
            if title ==book.get_title():
                book.return_book() ; return
    def show_books(self):
        for i in self.__books:
            a = i.get_details()
            print(f"{a['title']} by{a['author']} ({a['status']})")