def parzysta(x:int)->bool:
    if x%2==0:
        return True
    else:
        return False

wynik=parzysta(4)

if wynik==True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")