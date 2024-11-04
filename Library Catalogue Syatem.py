class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"You have checked out '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'. Thank you!")
        else:
            print(f"'{self.title}' was not checked out.")

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


class Library:
    def __init__(self):
        self.catalogue = []

    def add_book(self, book):
        self.catalogue.append(book)
        print(f"'{book.title}' by {book.author} has been added to the catalogue.")

    def list_books(self):
        if not self.catalogue:
            print("The catalogue is currently empty.")
        else:
            for book in self.catalogue:
                print(book)


library = Library()


book1 = Book("The Myth of Normal", "Gabor Maté")
book2 = Book("Daring Greatly", "Brené Brown")
book3 = Book("The Daily Stoic", "Ryan Holiday")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


print("\nCurrent Catalogue:")
library.list_books()


print("\nChecking out 'The Myth of Normal':")
book1.check_out()


print("\nTrying to check out 'The Myth of Normal' again:")
book1.check_out()


print("\nReturning 'The Myth of Normal':")
book1.return_book()


print("\nCatalogue after interaction:")
library.list_books()
