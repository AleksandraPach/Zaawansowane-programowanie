class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    def __str__(self) -> str:
        return f"{self._name} z oceną {self._marks}"
