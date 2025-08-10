import unittest
from tablero import Tablero, PosOcupadaException, PosInvalidaException
from jugador import Jugador
from tateti import Tateti

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
    
    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")
    
    def test_posicion_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "O")
    
    def test_posicion_invalida(self):
        with self.assertRaises(PosInvalidaException):
            self.tablero.poner_la_ficha(3, 0, "X")

class TestJugador(unittest.TestCase):
    def test_inicializacion(self):
        jugador = Jugador("Juan", "X")
        self.assertEqual(jugador.nombre, "Juan")
        self.assertEqual(jugador.ficha, "X")
        self.assertEqual(jugador.victorias, 0)
    
    def test_ganar_partida(self):
        jugador = Jugador("Ana", "X")
        jugador.ganar_partida()
        self.assertEqual(jugador.victorias, 1)
        self.assertEqual(jugador.partidas_jugadas, 1)

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.tateti = Tateti("Juan", "Pepe")
    
    def test_inicializacion(self):
        self.assertEqual(self.tateti.jugador1.nombre, "Juan")
        self.assertEqual(self.tateti.jugador2.nombre, "Pepe")
        self.assertEqual(self.tateti.jugador_actual, self.tateti.jugador1)
    
    def test_ocupar_casilla_cambia_turno(self):
        self.assertEqual(self.tateti.jugador_actual.ficha, "X")
        self.tateti.ocupar_casilla(0, 0)
        self.assertEqual(self.tateti.jugador_actual.ficha, "O")
    
    def test_victoria_fila(self):
        self.tateti.tablero.contenedor = [
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ]
        ganador = self.tateti.verificar_ganador()
        self.assertEqual(ganador, "X")
    
    def test_victoria_columna(self):
        """Test: detectar victoria en columna"""
        self.tateti.tablero.contenedor = [
            ["O", "X", "X"],
            ["O", "X", ""],
            ["O", "", ""]
        ]
        ganador = self.tateti.verificar_ganador()
        self.assertEqual(ganador, "O")
    
    def test_victoria_diagonal(self):
        """Test: detectar victoria en diagonal"""
        self.tateti.tablero.contenedor = [
            ["X", "O", "O"],
            ["O", "X", ""],
            ["", "", "X"]
        ]
        ganador = self.tateti.verificar_ganador()
        self.assertEqual(ganador, "X")
    
    def test_empate(self):
        """Test: detectar empate"""
        self.tateti.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.tateti.tablero_lleno())
        self.assertIsNone(self.tateti.verificar_ganador())
    
    def test_obtener_ganador_objeto(self):
        """Test: obtener objeto jugador ganador"""
        self.tateti.tablero.contenedor = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        ganador = self.tateti.obtener_ganador()
        self.assertEqual(ganador, self.tateti.jugador1)
    
    def test_finalizar_stats(self):
        """Test: finalizar partida actualiza estadísticas"""
        self.tateti.finalizar_partida(self.tateti.jugador1)
        self.assertEqual(self.tateti.jugador1.victorias, 1)
        self.assertEqual(self.tateti.jugador2.derrotas, 1)
    

if __name__ == '__main__':
    unittest.main()