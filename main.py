from datetime import date
from dieta import Dieta
from dietetyk import Dietetyk
from pacjent import Pacjent
from zamowienie import Zamowienie

p = Pacjent(1, "Tadeusz", "Zawarta", "Kasztanowa 13, Zawiercie", "niedoczynnosc tarczycy")
d = Dietetyk(2, "Joanna", "Zielona", "Katowice", "Dietix")
dietka1 = Dieta("Normal", 1500, 1200.15, 5)
dietka2 = Dieta("Zyj zdrowo", 2000, 1800.1555, 3)
z = Zamowienie()
z.pacjent = p
z.dietetyk = d
z.data = date(2022, 1, 12)
z.dieta = [dietka1, dietka2]

print(z)
print(z.obl_cene())
print(z.obl_kcal())
