import json
import socket
from game_logic import MemoryGame

HOST = "0.0.0.0"
PORT = 5000

def send_message(connection, data):
    message = json.dumps(data) + "\n"
    connection.sendall(message.encode("utf-8"))

def receive_message(file):
    line = file.readline()
    if not line:
        raise ConnectionError("El cliente se desconectó.")
    return json.loads(line)

def ask_server_move(game):
    while True:
        try:
            first = int(input("Primera carta (número): ")) - 1
            second = int(input("Segunda carta (número): ")) - 1
        except ValueError:
            print("Escribe dos números.")
            continue
        valid, message = game.play(1, first, second)
        print(message)
        if valid:
            return
        print("Inténtalo nuevamente:", message)

def run_server():
    game = MemoryGame(rows=4, cols=4)
    print("=== SERVIDOR - JUGADOR 1 ===")
    print(f"Esperando al cliente en el puerto {PORT}...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        connection, address = server_socket.accept()
        with connection:
            print(f"Cliente conectado desde: {address[0]}")
            connection_file = connection.makefile("r", encoding="utf-8")

            try:
                send_message(connection, {
                    "type": "welcome",
                    "message": "Conectado al Juego de Memoria. Eres el Jugador 2."
                })

                while not game.game_over:
                    send_message(connection, {
                        "type": "state",
                        "state": game.public_state()
                    })

                    if game.current_player == 1:
                        print("\nTu turno (Jugador 1 - Servidor).")
                        game.show_board()
                        ask_server_move(game)
                    else:
                        print("\nEsperando jugada del Jugador 2...")
                        while True:
                            request = receive_message(connection_file)
                            if request.get("type") != "play":
                                send_message(connection, {
                                    "type": "error",
                                    "message": "Solicitud no reconocida."
                                })
                                continue

                            picks = request.get("cards", [])
                            if not isinstance(picks, list) or len(picks) != 2:
                                send_message(connection, {
                                    "type": "error",
                                    "message": "Debes enviar exactamente dos posiciones."
                                })
                                continue

                            valid, message = game.play(2, picks[0], picks[1])
                            if valid:
                                print("Jugada del Jugador 2:", message)
                                break
                            send_message(connection, {
                                "type": "error",
                                "message": message
                            })

                send_message(connection, {
                    "type": "state",
                    "state": game.public_state()
                })
                print("\nPartida finalizada.")
                print("Puntuación:", game.scores)

            except (ConnectionError, OSError, json.JSONDecodeError) as error:
                print(f"\nConexión finalizada: {error}")
            finally:
                connection_file.close()

if __name__ == "__main__":
    run_server()
