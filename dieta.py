class Dieta:
    def __init__(self, nazwa_diety: str, kalorie: int, cena: float, ilosc_posilkow: int) -> None:
        self._nazwa_diety = nazwa_diety
        self._kalorie = kalorie
        self._cena = cena
        self._ilosc_posilkow = ilosc_posilkow

    def __str__(self) -> str:
        return f"nazwa diety: {self._nazwa_diety}, kcal: {self._kalorie}, " \
               f"cena: {self._cena}, ilosc posilkow w diecie: {self._ilosc_posilkow}"

    @property
    def nazwa_diety(self) -> str:
        return self._nazwa_diety

    @nazwa_diety.setter
    def nazwa_diety(self, nazwa_diety: str) -> None:
        self._nazwa_diety = nazwa_diety

    @property
    def kalorie(self) -> int:
        return self._kalorie

    @kalorie.setter
    def kalorie(self, kalorie) -> None:
        self._kalorie = kalorie

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, cena: float) -> None:
        self._cena = cena

    @property
    def ilosc_posilkow(self) -> int:
        return self._ilosc_posilkow

    @ilosc_posilkow.setter
    def ilosc_posilkow(self, ilosc_posilkow: int) -> None:
        self._ilosc_posilkow = ilosc_posilkow
