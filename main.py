from zad_2 import Library, Book, Student, Employee, Order

from datetime import date

from zad_3 import House, Flat

library1 = Library("Lublin", "Warszawska",
                   "12345", "8-16", "123456789")
library2 = Library("Krakow", "Kasztanowa",
                   "98765", "7-15", "987654321")

student1 = Student("Lusia", 60)
student2 = Student("Zosia", 10)
student3 = Student("Zbigniew", 77)

employee1 = Employee("Marian", "Lizak", date(2019, 12, 11),
                     date(1999, 1, 12), "Lublin",
                     "Zosinska", "32145", "456987432")
employee2 = Employee("Magda", "Sasinska",
                     date(2018, 6, 4), date(1998, 12, 19),
                     "Lublin", "Mariacka", "76523", "456987432")
employee3 = Employee("Lukasz", "Kisiel",
                     date(2010, 9, 8), date(1996, 5, 6),
                     "Krakow", "Wislana", "43278", "456987432")

book1 = Book(library2, date(2021, 11, 13),
             "Rafael", "Miguel", 251)
book2 = Book(library1, date(2019, 10, 19),
             "Witold", "Marciniak", 53)
book3 = Book(library2, date(2016, 3, 26),
             "Wiola", "Bieniek", 396)
book4 = Book(library1, date(1996, 7, 1),
             "Katarzyna", "Kosciniec", 123)
book5 = Book(library2, date(2018, 9, 30),
             "Monika", "Wawrzacz", 543)

order1 = Order(employee1, student2,
               [book1, book3], date(2021, 11, 22))
order2 = Order(employee3, student1,
               [book2, book4, book5], date(2021, 11, 21))

print(order1)
print(order2)

house = House(122.14, 4, 35000, "Katowice, Katowicka 14", 54)

flat = Flat(55.5, 2, 200000, "Mazancowice Mazan 1", 3)

print(house)
print(flat)
