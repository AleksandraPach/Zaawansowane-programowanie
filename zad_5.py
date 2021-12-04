def zawiera(lista: list, zmienna: int) -> bool:
    if zmienna in lista:
        return True
    else:
        return False


wynik = zawiera((2, 3, 4, 5), 10)

print(wynik)
