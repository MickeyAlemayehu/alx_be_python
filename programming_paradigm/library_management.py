class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

class Library:
        def __init__(self):
           self._books = []

        def add_book(self, book):
            self._books.append(book)
        def check_out_book(self, title):
            for book in self._books:
                if book.title == title and not book._is_checked_out:
                    book._is_checked_out = True
                    return f'You have checked out "{title}".'
            return f'Sorry, "{title}" is not available.'
        def return_book(self, title):
            for book in self._books:
                if book.title == title and book._is_checked_out:
                    book._is_checked_out = False
                    return f'You have returned "{title}".'
            return f'"{title}" was not checked out.'
        def list_available_books(self):
            available_books = []
            for book in self._books:
                if not book._is_checked_out:
                    available_books.append(f'{book.title} by {book.author}')
            for book_info in available_books:
                print(book_info)
