import os
from typing import List, Tuple

import numpy as np
import numpy.typing as npt

Board = npt.NDArray[np.int32]


class State(object):
    def __init__(self) -> None:
        self.board: Board = np.zeros([8, 8], dtype="int32")
        self.board[3, 3] = 1
        self.board[4, 3] = -1
        self.board[3, 4] = -1
        self.board[4, 4] = 1
        self.stack: List[Board] = []

    def is_finish(self, player) -> bool:
        if not np.any(self.board == 0):
            return True

        if len(self.legal_moves(player)) == 0:
            return True

        return False

    def make_attempt(self, player: int, x: int, y: int) -> None:
        assert self.is_legal_move(player, x, y)
        self.stack.append(self.board.copy())
        self.board[x, y] = player

    def cancel_attempt(self) -> None:
        self.board = self.stack.pop()

    def make_move(self, player: int, x: int, y: int) -> None:
        assert self.is_legal_move(player, x, y)
        self.board[x, y] = player

        # Again, the directions to check
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        # For each direction...
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and self.board[nx, ny] == -player:
                nx += dx
                ny += dy
                if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
                    while self.board[nx, ny] == -player:
                        nx += dx
                        ny += dy
                        # If we're off the board, we're done
                        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                            return

                    if self.board[nx, ny] == player:
                        while True:
                            nx -= dx
                            ny -= dy
                            if nx == x and ny == y:
                                break
                            self.board[nx, ny] = player

    def legal_moves(self, player: int) -> List[Tuple[int, int]]:
        moves = []
        for i in range(8):
            for j in range(8):
                # If the move is legal, add it to the list of legal moves
                if self.is_legal_move(player, i, j):
                    moves.append((i, j))
        return moves

    def is_legal_move(self, player: int, x: int, y: int) -> bool:
        # If the spot is not empty, it's not a legal move
        if self.board[x, y] != 0:
            return False

        # Directions to check for opponent's discs
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        # For each direction...
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and self.board[nx][ny] == -player:
                while True:  # Keep going in that direction
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        break
                    if self.board[nx, ny] == 0:
                        break
                    if self.board[nx, ny] == player:
                        return True
        return False

    def __str__(self) -> str:
        sep = "+-" * 8 + "+" + os.linesep
        ret = ""
        ret += sep
        for i in range(self.board.shape[0]):
            ret += "|"
            for j in range(self.board.shape[1]):
                if self.board[i, j] == 0:
                    ret += " "
                elif self.board[i, j] == 1:
                    ret += "o"
                elif self.board[i, j] == -1:
                    ret += "x"
                ret += "|"
            ret += os.linesep
            ret += sep
        return ret
