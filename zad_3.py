class Property:
    def __init__(self, area: float, rooms: int,
                 price: float, address: str) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return f""


class House (Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return f'Dom {super().__str__()} ' \
               f'o powierzchni działki {self._plot} '


class Flat(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return f'Mieszkanie {super().__str__()} na piętrze {self._floor} '


house = House(122.14, 4, 35000, "Katowice, Katowicka 14", 54)

flat = Flat(55.5, 2, 200000, "Mazancowice Mazan 1", 3)

print(house)
print(flat)
