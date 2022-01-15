from osoba import Osoba


class Pacjent(Osoba):
    def __init__(self, id_w_bazie: int, imie: str, nazwisko: str, adres: str, schorzenie: str) -> None:
        super().__init__(id_w_bazie, imie, nazwisko, adres)
        self._schorzenie = schorzenie

    def __str__(self) -> str:
        return f"{super().__str__()}, choroba: {self._schorzenie}"

    @property
    def schorzenie(self) -> str:
        return self._schorzenie

    @schorzenie.setter
    def schorzenie(self, schorzenie: str) -> None:
        self._schorzenie = schorzenie
