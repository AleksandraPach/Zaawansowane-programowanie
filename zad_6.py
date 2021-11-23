def bezdublikatow (lista1:list,lista2:list)->list:
    lista3=set(lista1+lista2)
    return [ x**3 for x in lista3]
    return lista3

wynik=bezdublikatow([2,3,4,5],[10,2])
print(wynik)