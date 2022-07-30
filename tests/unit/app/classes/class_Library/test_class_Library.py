import pytest
from app.classes.class_Library.class_Library import Book
from app.classes.class_Library.class_Library import Person
from app.classes.class_Library.class_Library import Reader
from app.classes.class_Library.class_Library import Library


@pytest.fixture
def some_book():
    book = Book("genre1", "title1", "author1")
    return book


@pytest.fixture
def some_person():
    person = Person("name2", "02.02.2002", "2222")
    return person


@pytest.fixture
def some_reader(some_book):
    reader = Reader("name1", 1, "01.01.2001", "1111", [some_book])
    return reader


@pytest.fixture
def some_library(some_reader, some_book):
    library = Library("address1", "library_phone1", [some_book], [some_reader])
    return library


@pytest.mark.parametrize(
    "expected_reader, expected_book, message", [(Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre1", "title1", "author1"), "name1 took title1"),
                                                (Reader("name2", 2, "02.02.2002", "2222", []),
                                                 Book("genre1", "title1", "author1"), "name2 is not member of library"),
                                                (Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre2", "title2", "author2"), "title2 unavailable")
                                                ]
)
def test_take_book(some_library, expected_reader: Reader, expected_book: Book, message: str):
    assert message == some_library.take_book(expected_reader, expected_book)


@pytest.mark.parametrize(
    "expected_reader, expected_book, message", [(Reader("name1", 1, "01.01.2001", "1111",
                                                        [Book("genre1", "title1", "author1")]),
                                                 Book("genre1", "title1", "author1"), "name1 returned title1"),
                                                (Reader("name2", 2, "02.02.2002", "2222", []),
                                                 Book("genre1", "title1", "author1"), "name2 is not member of library"),
                                                (Reader("name1", 1, "01.01.2001", "1111", []),
                                                 Book("genre2", "title2", "author2"), "title2 unavailable")
                                                ]
)
def test_return_book(some_library, expected_reader: Reader, expected_book: Book, message: str):
    assert message == some_library.return_book(expected_reader, expected_book)
