from tateti import Tateti
from tablero import PosOcupadaException, PosInvalidaException

def mostrar_tablero(tablero):
    print("  1   2   3")
    for i, fila in enumerate(tablero):
        print(f"{i + 1} {fila[0] or ' '} | {fila[1] or ' '} | {fila[2] or ' '}")
        if i < 2:
            print(" ---|---|---")
def main():
    player1 = input("Nombre Jugador 1 (X): ").strip() or "Jugador 1"
    player2 = input("Nombre Jugador 2 (O): ").strip() or "Jugador 2"

    tateti = Tateti(player1, player2)
    continuar = True
                
    while continuar:
        tateti.reiniciar_tablero()

        print("\n New game")

        if tateti.jugador1.partidas_jugadas > 0:
            print("Stats:")
            print(tateti.jugador1.stats())
            print(tateti.jugador2.stats())

        while True:
            mostrar_tablero(tateti.tablero.contenedor)
            print(f"\nTurno de {tateti.jugador_actual}")

            try:
                fil = int(input("Fila (1-3): "))
                col = int(input("Columna (1-3): "))
                tateti.ocupar_casilla((fil - 1), (col - 1))

                ganador = tateti.obtener_ganador()
                if ganador:
                    mostrar_tablero(tateti.tablero.contenedor)
                    print(f"\n{ganador.nombre} gano")
                    tateti.finalizar_partida(ganador)
                    break
                
                if tateti.tablero_lleno():
                    mostrar_tablero(tateti.tablero.contenedor)
                    print("Empate")
                    tateti.finalizar_partida("empate")
                    break

            except (PosOcupadaException, PosInvalidaException) as e:
                print(f"Error: {e}")
            except ValueError:
                print("Ingrese numeros validos (1-3)")
            except Exception as e:
                print(f"Error: {e}")
        
        print("\n Stats")
        print(tateti.jugador1.stats())
        print(tateti.jugador2.stats())

        respuesta = input("\nSale otra? (y/n): ").strip().lower()
        continuar = respuesta == "y"

if __name__ == "__main__":
    main()