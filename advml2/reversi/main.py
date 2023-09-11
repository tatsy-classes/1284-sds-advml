import time
import tkinter as tk

import numpy as np

from advml.reversi.gui import Gui
from advml.reversi.state import State

score_board = np.array(
    [
        [100, -40, 20, 5, 5, 20, -40, 100],
        [-40, -80, -1, -1, -1, -1, -80, -40],
        [20, -1, 5, 1, 1, 5, -1, 20],
        [5, -1, 1, 0, 0, 1, -1, 5],
        [5, -1, 1, 0, 0, 1, -1, 5],
        [20, -1, 5, 1, 1, 5, -1, 20],
        [-40, -80, -1, -1, -1, -1, -80, -40],
        [100, -40, 20, 5, 5, 20, -40, 100],
    ],
    dtype="int32",
)


def mini_max(state: State, player: int, depth: int, max_depth: int = 3) -> int:
    if depth == max_depth:
        return player * np.sum(state.board * score_board)

    best_score = -99999
    for move in state.legal_moves(player):
        state.make_attempt(player, move[0], move[1])
        score = -mini_max(state, -player, depth + 1, max_depth)
        state.cancel_attempt()
        if score > best_score:
            best_score = score

    return best_score


def mini_max_move(state: State, player: int, max_depth: int = 3):
    best_move = (0, 0)
    best_score = -99999
    for move in state.legal_moves(player):
        state.make_attempt(player, move[0], move[1])
        score = -mini_max(state, -player, 0, max_depth)
        state.cancel_attempt()
        if score > best_score:
            best_move = move
            best_score = score

    return best_move


def random_move(state: State, player: int):
    moves = state.legal_moves(player)
    idx = np.random.randint(0, len(moves))
    return moves[idx]


def main() -> None:
    root = tk.Tk()
    gui = Gui(master=root)

    state = State()
    player = 1
    while not state.is_finish(player):
        if player == 1:
            move = random_move(state, player)
        elif player == -1:
            move = mini_max_move(state, player)

        state.make_move(player, move[0], move[1])
        player = -player
        gui.draw(state.board)
        time.sleep(1)

    print(state)

    gui.mainloop()


if __name__ == "__main__":
    main()
