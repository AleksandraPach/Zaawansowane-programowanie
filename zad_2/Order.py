from datetime import date

from zad_2 import Employee, Student, Book


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list[Book], order_date: date) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return "Pracownik {} obsłużył studenta {}. Zamówienie z dnia " \
               "{} na {}.".format(self._employee, self._student,
                                  self._order_date, *self._books)
