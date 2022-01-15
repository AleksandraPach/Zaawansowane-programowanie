from pacjent import Pacjent
from dietetyk import Dietetyk
from dieta import Dieta
from datetime import date


class Zamowienie:
    def __init__(self) -> None:
        self._pacjent = None
        self._dietetyk = None
        self._data = None
        self._dieta = None

    def __str__(self) -> str:
        return f"Pacjent: {self._pacjent}, \ndietetyk: {self._dietetyk}, " \
               f"data zamowienia: {self._data}, \nzamówione diety:{[str(X) for X in self._dieta]}"

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent) -> None:
        self._pacjent = pacjent

    @property
    def dietetyk(self) -> Dietetyk:
        return self._dietetyk

    @dietetyk.setter
    def dietetyk(self, dietetyk: Dietetyk) -> None:
        self._dietetyk = dietetyk

    @property
    def data(self) -> date:
        return self._data

    @data.setter
    def data(self, data: date):
        self._data = data

    @property
    def dieta(self) -> list[Dieta]:
        return self._dieta

    @dieta.setter
    def dieta(self, dieta: list[Dieta]) -> None:
        self._dieta = dieta

    def obl_cene(self) -> float:
        wartosc = 0.00
        for pp in self.dieta:
            wartosc += pp.cena
        return round(wartosc, 2)

    def obl_kcal(self) -> int:
        kcal = 0
        for kc in self.dieta:
            kcal += kc.kalorie
        return kcal
