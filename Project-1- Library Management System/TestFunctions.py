from Book import Book
from Catalog import Catalog
from User import Member, Librarian

librarian = Librarian("Awantik","Banglore",34,"qwrrwer","7584")
print(librarian.__repr__())

m1 = Member("vishesh","Banglore",20,"hshdfdsj","1234")
print(m1.__repr__())

b = librarian.addBook("The Ultimate Gift","Jim Stoval",12,"2020-12-07",200)
librarian.addBookItem(b,"H123")
librarian.addBookItem(b,"H128")
librarian.addBookItem(b,"H129")
librarian.Catalog.displayAllBooks()
print(librarian.Catalog.books)
b2 = librarian.addBook("The Secret","qwe",34,"2020-08-14",350)
librarian.addBookItem(b2,"A123")
librarian.addBookItem(b2,"A56")
librarian.addBookItem(b2,"A134")
librarian.Catalog.displayAllBooks()
print(librarian.Catalog.books)
m1.issueBook("The Secret")
librarian.Catalog.displayAllBooks()
m1.returnBook("The Secret")
librarian.Catalog.displayAllBooks()
print(m1.Catalog.books)
m1.Catalog.displayAllBooks()
librarian.removeBook("The Secret")
librarian.Catalog.displayAllBooks()