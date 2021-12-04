liczba = [2, 4, 5, 1, 6]


def mnoznik_for(liczba):
    for x in range(len(liczba)):
        liczba[x] = liczba[x] * 2
        return(liczba[x])


print(mnoznik_for(liczba))
