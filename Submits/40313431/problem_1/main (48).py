class Book:
    status = 'Available'
    def __init__(self,title,author,status):
        self.title = title
        self.author = author
        self.status = status
    def get_details(self):
        return f"{self.title} by {self.author}({self.status})"
    def borrow (self) :
        self.status = 'Borrowed'
    def returnn (self):
        self.status = 'Available'


class Library(Book):
    show = []
    def __init__(self,title,author,status):
        super().__init__(self,title,author,status)
    def borrow_book (self) :
        self.borrow()
    def return_book(self):
        self.returnn()




request = input()
books = []
finalr = ""


while request != 'END' :
    desireresult = ""



    if 'ADD' in request :
        desireresult1 = ""
        desireresult2 = ""
        i=5
        while request[i]!= '"' :
            desireresult1 += request[i]
            i += 1
        i += 3
        while request[i]!= '"' :
            desireresult2 += request[i]
            i+=1


        #r = request.split()
        #r[1] = r[1].strip('"')
        #r[2] =  r[2].strip('"')
        Book(desireresult1,desireresult2,'Available')
        books.append(Book(desireresult1,desireresult2,'Available'))
        finalr += f"Added {desireresult1} by {desireresult2}"



    if 'BORROW' in request :
        i= 8
        while request[i]!= '"' :
            desireresult += request[i]
            i += 1

        #desireresult = desireresult.strip('"')
        for j in range(len(books)) :

            if  books[j].title == desireresult :
                books[j].borrow()
                finalr += f"Borrowed {desireresult}"



    if 'RETURN' in request :
        i= 8
        while request[i]!= '"' :
            desireresult += request[i]
            i += 1

        #desireresult = desireresult.strip('"')
        for j in range(len(books)) :

            if desireresult == books[j].title:
                books[j].returnn()
                finalr += f"Returned {desireresult}"



    if request == 'SHOW' :
        finalr += 'Library Books\n'
        for k in range(len(books)) :
            w = books[k].get_details()
            finalr += ' '
            finalr += w
            finalr += "\n"


    request = input()
    finalr += "\n"

print(finalr)