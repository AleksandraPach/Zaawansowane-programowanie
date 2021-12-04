lista: list = [2, 4, 5, 1, 6]


def mnoznik_lista(lista: list):
    liczby = [x * 2 for x in lista]
    return(liczby)


print(mnoznik_lista(lista))
