from datetime import date

class Pojazd:
    def __init__(self, marka:str, typ:str, moc_silnika:int, kolor:str, rocznik:date.year) -> None:
        self._marka = marka
        self._typ=typ
        self._moc_silnika=moc_silnika
        self._kolor=kolor
        self._rocznik=rocznik

    def __str__(self):
        return f"marka: {self._marka}, typ: {self._typ}, " \
               f" moc silnika: {self._moc_silnika} konii mechanicznych, " \
               f"\nkolor: {self._kolor}, rocznik: {self._rocznik}"

    @property
    def marka(self) -> None:
        return self._marka

    @marka.setter
    def marka(self, marka: str) -> None:
        self._marka = marka

    @property
    def typ(self) -> None:
        return self._typ

    @typ.setter
    def typ(self, typ: str) -> None:
        self._typ = typ

    @property
    def moc_silnika(self) -> None:
        return self._moc_silnika

    @moc_silnika.setter
    def moc_silnika(self, moc_silnika: int) -> None:
        self._moc_silnika = moc_silnika

    @property
    def kolor(self) -> None:
        return self._kolor

    @kolor.setter
    def kolor(self, kolor: str) -> None:
        self._kolor = kolor

    @property
    def rocznik(self) -> None:
        return self._rocznik

    @rocznik.setter
    def rocznik(self, rocznik: date.year) -> None:
        self._rocznik = rocznik

class Firma:
    def __init__(self, nazwa:str, rok_powstania:date.year, zatrudnieni:int, nr_tel:int) -> None:
        self._nazwa = nazwa
        self._rok_powstania = rok_powstania
        self._zatrudnieni = zatrudnieni
        self._nr_tel = nr_tel

    def __str__(self):
        return f"{self._nazwa}, powstała w roku {self._rok_powstania}, " \
                f"ilość pracowników: {self._zatrudnieni}, " \
               f"nr telefonu: {self._nr_tel}, "

    @property
    def nazwa(self) -> None:
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nazwa: str) -> None:
        self._nazwa = nazwa

    @property
    def rok_powstania(self) -> None:
        return self._rok_powstania

    @rok_powstania.setter
    def rok_powstania(self, rok_powstania: date.year) -> None:
        self._rok_powstania = rok_powstania

    @property
    def zatrudnieni(self) -> None:
        return self._zatrudnieni

    @zatrudnieni.setter
    def zatrudnieni(self, zatrudnieni: int) -> None:
        self._zatrudnieni = zatrudnieni

    @property
    def nr_tel(self) -> None:
        return self._nr_tel

    @nr_tel.setter
    def nr_tel(self, nr_tel: int) -> None:
        self._nr_tel = nr_tel

class FirmaTransportowa(Firma):
    def __init__(self, nazwa:str, rok_powstania:date.year, zatrudnieni:int, nr_tel:int, godziny_kursów:str) -> None:
        super().__init__(nazwa, rok_powstania, zatrudnieni, nr_tel)
        self._godziny_kursów=godziny_kursów

    def __str__(self) -> str:
        return f"{super().__str__()} godziny wykonywania kursów: {self._godziny_kursów}, \n"
    @property
    def godziny_kursów(self)->None:
        return self._godziny_kursów

    @godziny_kursów.setter
    def godziny_kursów(self, godziny_kursów:str)->None:
        self._godziny_kursów=godziny_kursów

class FirmaSpozywca(Firma):
    def __init__(self, nazwa:str, rok_powstania:date.year, zatrudnieni:int, nr_tel:int, godziny_odbioru:str)->None:
        super().__init__(nazwa, rok_powstania, zatrudnieni, nr_tel)
        self._godziny_odbioru=godziny_odbioru

    def __str__(self) -> str:
        return f"{super().__str__()} godziny odbioru produktów: {self._godziny_odbioru}"

    @property
    def godziny_odbioru(self) -> None:
        return self._godziny_odbioru

    @godziny_odbioru.setter
    def godziny_odbioru(self, godziny_odbioru: str) -> None:
        self._godziny_odbioru = godziny_odbioru

class Odcinek:
    def __init__(self, m1:str, m2:str, odleglosc:float, platny_odc:bool, czas:str) -> None:
        self._m1 = m1
        self._m2 = m2
        self._odleglosc = odleglosc
        self._platny_odc = platny_odc
        self._czas = czas

    def __str__(self) -> str:
        if self._platny_odc==0: return f"z {self._m1} do {self._m2}," \
                   f"gdzie trasa nie zawiera płatnych odcinków, czas kursu: {self._czas} godziny"
        if self._platny_odc==1: return f"z {self._m1} do {self._m2}," \
                   f"gdzie trasa zawiera płatne odcinki, czas kursu: {self._czas} godziny"

class Kurs:
    def __init__(self) -> None:
        self._firmaT = None
        self._firmaS = None
        self._odcinek = None
        self._pojazd = None
        self._status = None

    def __str__(self) -> str:
        return f"Firma transportowa {self._firmaT} dostarcza do firmy spożywczej {self._firmaS} \n" \
               f"na odcinkach {[str(X) for X in self._odcinek]}, \n" \
               f"używając pojazdu: {self._pojazd}, status kursu: {self._status}."

    @property
    def firmaT(self) -> None:
        return self._firmaT

    @firmaT.setter
    def firmaT(self, firmaT: FirmaTransportowa) -> None:
        self._firmaT = firmaT

    @property
    def firmaS(self) -> None:
        return self._firmaS

    @firmaS.setter
    def firmaS(self, firmaS:FirmaSpozywca) -> None:
        self._firmaS = firmaS

    @property
    def odcinek(self) -> None:
        return self._odcinek

    @odcinek.setter
    def odcinek(self, odcinek: list[Odcinek]) -> None:
        self._odcinek = odcinek

    @property
    def pojazd(self) -> None:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, pojazd: Pojazd) -> None:
        self._pojazd = pojazd

    @property
    def status(self)->None:
        return self._status

    @status.setter
    def status(self, status:str):
        self._status=status

    def obl_km(self) -> float:
        wartosc = 0.0
        for x in range(len(self.odcinek)):
            wartosc = round(wartosc+self.odcinek[x]._odleglosc,2)
        return wartosc

    def marka_p(self) -> str:
        return (self.pojazd._marka)

p1=Pojazd("Fiat","samochód ciężarowy", 234,"czerwony",2015)
o1=Odcinek("Katowice","Chorzów",52.23,0,"2.5")
o2=Odcinek("Zywiec","Bielsko-Biała",71.2111,1,"1.5")
fT1=FirmaTransportowa("Zawix",2000,15,12345672345,"8-20")
fS1=FirmaSpozywca("ABC",2011,30,1298765443,"9-16")

k1=Kurs()
k1.pojazd=p1
k1.odcinek=[o1, o2]
k1.firmaT=fT1
k1.firmaS=fS1
k1.status="zaplanowany"

print(k1)
print(k1.obl_km())
print(k1.marka_p())