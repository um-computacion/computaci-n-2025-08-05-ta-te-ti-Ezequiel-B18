from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, nombre_j1="Jugador 1", nombre_j2="Jugador 2"):
        self.jugador1 = Jugador(nombre_j1, "X")
        self.jugador2 = Jugador(nombre_j2, "O")
        self.jugador_actual = self.jugador1
        self.tablero = Tablero()

    def ocupar_casilla(self, fil, col):
        # pongo la ficha
        self.tablero.poner_la_ficha(fil, col, self.jugador_actual.ficha)
        # cambia jugador
        if self.jugador_actual == self.jugador1:
            self.jugador_actual = self.jugador2
        else:
            self.jugador_actual = self.jugador1

    def verificar_ganador(self):
        tablero = self.tablero.contenedor

        # verifica filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]

        # verifica columnas
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != "":
                return tablero[0][col]
            
        # verificar diagonales

        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
            return tablero[0][2]
        
        return None
    
    def obtener_ganador(self):
        ficha_ganadora = self.verificar_ganador()
        if ficha_ganadora == self.jugador1.ficha:
            return self.jugador1
        elif ficha_ganadora == self.jugador2.ficha:
            return self.jugador2
        return None

    def finalizar_partida(self, resultado):
        if resultado == "empate":
            self.jugador1.empatar_partida()
            self.jugador2.empatar_partida()
        elif resultado == self.jugador1:
            self.jugador1.ganar_partida()
            self.jugador2.perder_partida()
        elif resultado == self.jugador2:
            self.jugador2.ganar_partida()
            self.jugador1.perder_partida()

    def reiniciar_tablero(self):
        self.tablero = Tablero()
        self.jugador_actual = self.jugador1

    def tablero_lleno(self):
        for fila in self.tablero.contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        return True