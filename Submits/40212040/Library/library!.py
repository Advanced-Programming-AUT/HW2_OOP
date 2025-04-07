class Book:
    def __init__(self,title,author,status='available'):
        self.title=title
        self.authors=author
        self.status=status
    def borrow(self):
        if self.status == 'available':
            self.status='borrowed'
            print(f'{self.title} is borrowed')
        else:
            print(f'{self.title} is not available now')

    def return_book(self):
        if self.status == 'borrowed':
            self.status = 'available'
            print(f'returned successfully! {self.title} is available now')
        else:
            print('Invalid, the following book is already available & has not been borrowed lately')
    def get_details(self):
        print(f'name: {self.title},author: {self.authors},status: {self.status}')

class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title,author):
        self.books.append(Book(title,author))
        print(f'added book {title} by {author}')
    def borrow_book(self,book):
        book.borrow()
    def return_borrowed_book(self,book):
        book.return_book()
    def show_books(self):
        for t in self.books:
            t.get_details()
            #print(':)')

l=[]
x=input()
while(True):
    if not x:
        break
    else:
        l.append(x)
        x=input()
L=Library()
for item in l:
    y=item.split('"')

    match y[0]:
        case 'ADD ':
            y[1].strip()
            y[3].strip()
            L.add_book(y[1],y[3])
        case 'BORROW ':
            y[1].strip()
            for it in L.books:
                if it.title == y[1]:
                    L.borrow_book(it)
        case 'RETURN ' :
            y[1].strip()
            for it in L.books:
                if it.title == y[1]:
                    L.return_borrowed_book(it)
        case 'SHOW':
            L.show_books()
