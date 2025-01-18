
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def return_book(self):
        self._is_checked_out = True

    def is_checked_out(self):
        return self._is_checked_out
    
    def check_in(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.return_book()
                return True
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.check_in()
                return True
        return False
    
    def list_available_books(self):
        available_books = []
        for book in self._books:
            if not book.is_checked_out():
                available_books.append(f"{book.title} by {book.author}")
        return available_books
