from zad_3 import Property


class House (Property):
    def __init__(self, area: float, rooms: int,
                 price: float, address: str, plot: int) -> None:
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return f'Dom {super().__str__()} ' \
               f'o powierzchni działki {self._plot} '
