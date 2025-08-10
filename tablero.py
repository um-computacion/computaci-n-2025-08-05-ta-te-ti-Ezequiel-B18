class PosOcupadaException(Exception):
    ...
class PosInvalidaException(Exception):
    ...

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        # ver si esta esa posicion en el tablero o fuera de el
        if fil < 0 or fil > 2 or col < 0 or col > 2:
            raise PosInvalidaException("Fuera del tablero")
        # ver si esta ocupado...
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posicion ocupada")