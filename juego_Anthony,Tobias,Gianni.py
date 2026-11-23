from game_logic import MemoryGame

def run_local():
    game = MemoryGame()
    print(" JUEGO DE MEMORIA - MODO LOCAL ")
    print("Selecciona las posiciones numeradas del tablero.")
    while not game.game_over:
        game.show_board()
        print(f"\nTurno del Jugador {game.current_player}")
        try:
            first = int(input("Primera carta: ")) - 1
            second = int(input("Segunda carta: ")) - 1
        except ValueError:
            print("Entrada no válida. Escribe números.")
            continue

        valid, message = game.play(game.current_player, first, second)
        print(message)
        if valid and not game.game_over:
            game.show_board()
            game.reveal_last_picks()

    game.show_board()
    print("\n RESULTADO FINAL ")
    print(f"Jugador 1: {game.scores[1]} parejas")
    print(f"Jugador 2: {game.scores[2]} parejas")
    if game.scores[1] > game.scores[2]:
        print("Ganador: Jugador 1")
    elif game.scores[2] > game.scores[1]:
        print("Ganador: Jugador 2")
    else:
        print("Resultado: empate")

if __name__ == "__main__":
    run_local()
