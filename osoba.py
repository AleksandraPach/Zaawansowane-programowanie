class Osoba:
    def __init__(self, id_w_bazie: int, imie: str, nazwisko: str, adres: str) -> None:
        self._id_w_bazie = id_w_bazie
        self._imie = imie
        self._nazwisko = nazwisko
        self._adres = adres

    def __str__(self) -> str:
        return f"id: {self._id_w_bazie}, " \
               f"imie i nazwisko: {self._imie} {self._nazwisko}, adres:{self._adres}"

    @property
    def id_w_bazie(self) -> int:
        return self._id_w_bazie

    @id_w_bazie.setter
    def id_w_bazie(self, id_w_bazie: int) -> None:
        self._id_w_bazie = id_w_bazie

    @property
    def imie(self) -> str:
        return self._imie

    @imie.setter
    def imie(self, imie: str) -> None:
        self._imie = imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko: str) -> None:
        self._nazwisko = nazwisko

    @property
    def adres(self) -> str:
        return self._adres

    @adres.setter
    def adres(self, adres: str) -> None:
        self._adres = adres
