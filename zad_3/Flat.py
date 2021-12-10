from zad_3 import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, floor: int) -> None:
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return f'Mieszkanie {super().__str__()} na piętrze {self._floor} '
