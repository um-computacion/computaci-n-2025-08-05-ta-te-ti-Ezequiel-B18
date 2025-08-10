class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.victorias = 0
        self.derrotas = 0
        self.empates = 0
        self.partidas_jugadas = 0

    def ganar_partida(self):
        self.victorias += 1
        self.partidas_jugadas += 1
    
    
    def perder_partida(self):
        self.derrotas += 1
        self.partidas_jugadas += 1

    def empatar_partida(self):
        self.empates += 1
        self.partidas_jugadas += 1

    def stats(self):
        if self.partidas_jugadas == 0:
            return f"{self.nombre}: No ha jugado"
        
        porcentaje_victorias = (self.victorias / self.partidas_jugadas) * 100
        return f"{self.nombre} ({self.ficha}): {self.victorias}G {self.derrotas}P {self.empates}E - {porcentaje_victorias:.1f}% victorias"
    
    def __str__(self):
        return f"{self.nombre} ({self.ficha})"