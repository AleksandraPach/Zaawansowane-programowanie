class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str) -> None:
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"w mieście {self._city}, na ulicy {self._street}, " \
               f"kod pocztowy {self._zip_code}." \
               f" Jest otwarta w godzinach {self._open_hours}. " \
               f"W razie kontaktu," \
               f" nr telefonu to: {self._phone}"
