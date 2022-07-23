class Book:
    genre = None
    title = None
    author = None

    def __init__(self, genre: str, title: str, author: str):
        self.genre = genre
        self.title = title
        self.author = author


class Reader:
    full_name = None
    readers_card = None
    date_of_birth = None
    personal_phone = None

    def __init__(self, full_name: str, readers_card:str, date_of_birth: str, personal_phone: str):
        self.full_name = full_name
        self.readers_card = readers_card
        self.date_of_birth = date_of_birth
        self.personal_phone_number = personal_phone


class Library:
    address = None
    library_phone = None
    books_available = []
    readers = []
    books_taken = []

    def __init__(self, address: str, library_phone: str, books_available: list, readers: list):
        self.address = address
        self.library_phone = library_phone
        self.books_available = books_available
        self.readers = readers

    def take_book(self, reader: Reader, books_taken: list):
        if books_taken in self.books_available:
            return f'{reader.full_name} took {books_taken}'
        else:
            return f'{books_taken} unavailable'

    def return_book(self, reader: Reader, books_returned: list):
        return f'{reader.full_name} returned {books_returned}'

    def status(self):
        return f'{self.readers} got {self.books_taken}'
