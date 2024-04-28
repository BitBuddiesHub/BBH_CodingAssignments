class Library:
    
    total_books = 0

    def __init__(self, name, books):
        self.name = name
        self.books = books
        Library.total_books += len(books)
        
    @classmethod
    def display_total_books(cls):
        # TODO: Create a class method that prints the total number of books in all libraries
        print (f'Total books in all libraries: {cls.total_books}')

    @staticmethod
    def info():
        # TODO: Create a static method that prints information about what a library is
        print ("A library is a collection of books and resources in digital or printed formats that is organized for use and maintained by a public body, an institution, or a private individual.")

    def add_book(self, new_book):
        # TODO: Create an instance method that adds a new book to the library's list of books
        # TODO: Update the `total_books` class variable to reflect the addition of a new book
        self.books.append(new_book)
        Library.total_books += 1