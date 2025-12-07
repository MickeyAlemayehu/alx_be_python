class Book:
    """
    Base class representing a book with title and author.
    """
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size attribute.
    """
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page_count attribute.
    """
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A library class that uses composition to manage a collection of books.
    """
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book (Book, EBook, or PrintBook) to the library.
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        Formats output differently based on book type.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")

