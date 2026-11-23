import random
import time

class MemoryGame:
    def __init__(self, rows=4, cols=4):
        if rows * cols % 2 != 0:
            raise ValueError("El tablero debe tener un número par de cartas.")
        self.rows = rows
        self.cols = cols
        self.total = rows * cols
        self.cards = self._create_cards()
        self.matched = set()
        self.scores = {1: 0, 2: 0}
        self.current_player = 1
        self.game_over = False
        self.last_picks = []
        self.message = "Comienza el Jugador 1."

    def _create_cards(self):
        pairs = self.total // 2
        values = list(range(1, pairs + 1)) * 2
        random.shuffle(values)
        return values

    def play(self, player, first, second):
        if self.game_over:
            return False, "La partida ya terminó."
        if player != self.current_player:
            return False, "No es el turno de ese jugador."
        if first == second:
            return False, "Debes seleccionar dos cartas diferentes."
        if not (0 <= first < self.total and 0 <= second < self.total):
            return False, "Selecciona posiciones válidas."
        if first in self.matched or second in self.matched:
            return False, "Una de esas cartas ya está descubierta."

        self.last_picks = [first, second]
        if self.cards[first] == self.cards[second]:
            self.matched.update([first, second])
            self.scores[player] += 1
            result = "¡Pareja encontrada! Se suma un punto."
        else:
            result = "Las cartas no coinciden."

        self.game_over = len(self.matched) == self.total
        if self.game_over:
            result += " La partida ha terminado."
        else:
            self.current_player = 2 if player == 1 else 1
            result += f" Ahora juega el Jugador {self.current_player}."

        self.message = result
        return True, result

    def public_state(self):
        visible = {}
        for index in self.matched:
            visible[index] = self.cards[index]

        # Las dos últimas cartas se muestran en el estado para que ambos
        # jugadores puedan observar el resultado del turno.
        for index in self.last_picks:
            visible[index] = self.cards[index]

        winner = None
        if self.game_over:
            if self.scores[1] > self.scores[2]:
                winner = 1
            elif self.scores[2] > self.scores[1]:
                winner = 2
            else:
                winner = 0

        return {
            "rows": self.rows,
            "cols": self.cols,
            "total": self.total,
            "visible": visible,
            "matched": sorted(self.matched),
            "scores": self.scores,
            "current_player": self.current_player,
            "game_over": self.game_over,
            "winner": winner,
            "message": self.message,
        }

    def show_board(self):
        visible = self.public_state()["visible"]
        print("\nTablero:")
        for index in range(self.total):
            if index in visible:
                value = str(visible[index])
            else:
                value = "##"
            print(f"{index + 1:02d}:{value:>2}", end="   ")
            if (index + 1) % self.cols == 0:
                print()
        print(f"Puntos - Jugador 1: {self.scores[1]} | Jugador 2: {self.scores[2]}")

    def reveal_last_picks(self):
        if len(self.last_picks) == 2:
            time.sleep(1.5)
            self.last_picks = []
