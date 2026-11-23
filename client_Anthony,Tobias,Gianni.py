import json
import socket

PORT = 5000

def send_message(connection, data):
    connection.sendall((json.dumps(data) + "\n").encode("utf-8"))

def receive_message(file):
    line = file.readline()
    if not line:
        raise ConnectionError("El servidor cerró la conexión.")
    return json.loads(line)

def show_state(state):
    rows = state["rows"]
    cols = state["cols"]
    visible = {int(k): v for k, v in state["visible"].items()}

    print("\n=== TABLERO ===")
    for index in range(state["total"]):
        value = str(visible[index]) if index in visible else "##"
        print(f"{index + 1:02d}:{value:>2}", end="   ")
        if (index + 1) % cols == 0:
            print()

    print(f"Puntos - Jugador 1: {state['scores']['1']} | "
          f"Jugador 2: {state['scores']['2']}")
    print(state["message"])

def run_client():
    server_ip = input("IP del equipo que ejecuta el servidor: ").strip()
    print(f"Conectando con {server_ip}:{PORT}...")

    try:
        with socket.create_connection((server_ip, PORT), timeout=10) as connection:
            connection.settimeout(None)
            connection_file = connection.makefile("r", encoding="utf-8")

            welcome = receive_message(connection_file)
            print(welcome.get("message", "Conectado."))

            state = None
            while True:
                response = receive_message(connection_file)

                if response.get("type") == "error":
                    print("Aviso del servidor:", response.get("message"))
                    if state and state["current_player"] == 2:
                        try:
                            first = int(input("Primera carta: ")) - 1
                            second = int(input("Segunda carta: ")) - 1
                            send_message(connection, {
                                "type": "play",
                                "cards": [first, second]
                            })
                        except ValueError:
                            print("Escribe números válidos.")
                    continue

                if response.get("type") != "state":
                    continue

                state = response["state"]
                show_state(state)

                if state["game_over"]:
                    print("\n=== RESULTADO FINAL ===")
                    if state["winner"] == 0:
                        print("La partida terminó en empate.")
                    else:
                        print(f"Ganador: Jugador {state['winner']}")
                    break

                if state["current_player"] == 2:
                    while True:
                        try:
                            first = int(input("Primera carta: ")) - 1
                            second = int(input("Segunda carta: ")) - 1
                            send_message(connection, {
                                "type": "play",
                                "cards": [first, second]
                            })
                            break
                        except ValueError:
                            print("Escribe números válidos.")

            connection_file.close()

    except (OSError, ConnectionError, json.JSONDecodeError) as error:
        print(f"No se pudo completar la conexión: {error}")
        print("Verifica que el servidor esté activo y que ambos equipos "
              "estén conectados a la misma red LAN.")

if __name__ == "__main__":
    run_client()
