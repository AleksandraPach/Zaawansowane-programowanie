from datetime import date

from zad_2 import Library


class Book:
    def __init__(self, library: Library, publication_date: date,
                 author_name: str, author_surname: str,
                 number_of_pages: int) -> None:
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Książka dostępna w bibliotece {self._library}, " \
               f"napisana przez {self._author_name} {self._author_surname}, " \
               f"wydana {self._publication_date}, " \
               f"zawiera {self._number_of_pages} stron"
