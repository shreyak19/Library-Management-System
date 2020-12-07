from Book import Book
from Catalog import Catalog
class User:
    Catalog = Catalog()
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.book_issued = ""
        self.bookitem = None
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days=10):
        b = User.Catalog.searchByName(name)
        if b:
            if b.total_count > 0:
                bookitem = b.book_item[-1]
                User.Catalog.removeBookItem(name,bookitem.rack)
                self.book_issued = name
                self.bookitem = bookitem
                

    
    #assume name is unique
    def returnBook(self,name):
        if self.book_issued:
            b = User.Catalog.searchByName(name)
            User.Catalog.addBookItem(b,self.bookitem.rack)
        else:
            print("No book is issued by customer")
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name +"  "+ self.location +"  "+ self.emp_id
    
    def addBook(self,name,author,isbn,publish_date,pages):
        return User.Catalog.addBook(name,author,isbn,publish_date,pages)
    
    def addBookItem(self,book,rack):
        User.Catalog.addBookItem(book,rack)
    
    def removeBook(self,name):
        b = User.Catalog.searchByName(name)
        if b:
            User.Catalog.books.remove(b)
            User.Catalog.different_book_count -= 1
    
    def removeBookItemFromCatalog(self,catalog,book,rack):
        User.Catalog.removeBookItem(book,rack)
    