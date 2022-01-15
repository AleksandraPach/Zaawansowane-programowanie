from osoba import Osoba


class Dietetyk(Osoba):
    def __init__(self, id_w_bazie: int, imie: str, nazwisko: str, adres: str, nazwa_firmy: str) -> None:
        super().__init__(id_w_bazie, imie, nazwisko, adres)
        self._nazwa_firmy = nazwa_firmy

    def __str__(self) -> str:
        return f"{super().__str__()}, nazwa firmy: {self._nazwa_firmy}"

    @property
    def nazwa_firmy(self) -> str:
        return self._nazwa_firmy

    @nazwa_firmy.setter
    def nazwa_firmy(self, nazwa_firmy: str) -> None:
        self._nazwa_firmy = nazwa_firmy
