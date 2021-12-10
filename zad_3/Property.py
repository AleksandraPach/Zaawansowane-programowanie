class Property:
    def __init__(self, area: float, rooms: int,
                 price: float, address: str) -> None:
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return f""
