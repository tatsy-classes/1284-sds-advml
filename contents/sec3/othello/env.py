from __future__ import annotations

import os
from enum import Enum
from typing import Any, Dict, List, Tuple, Union

import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from IPython.core.pylabtools import print_figure

Board = npt.NDArray[np.object_]


class Player(Enum):
    NONE = 0
    BLACK = 1
    WHITE = -1

    def next(self) -> Player:
        assert self.value != 0

        if self == Player.BLACK:
            return Player.WHITE
        else:
            return Player.BLACK

    def __repr__(self) -> str:
        return str(self.value)


class Move(object):
    def __init__(self, player: Player, x: int, y: int) -> None:
        assert 0 <= x <= 8 and 0 <= y <= 8

        self.player = player
        self.x = x
        self.y = y

    def is_pass(self):
        return self.x < 0 and self.y < 0

    @staticmethod
    def Pass(player: Player):
        move = Move(player, 0, 0)
        move.x, move.y = -1, -1
        return move

    def __eq__(self, other) -> bool:
        if self.player != other.player:
            return False
        if self.x != other.x:
            return False
        return self.y != other.y

    def __repr__(self) -> str:
        assert self.player in [Player.BLACK, Player.WHITE]
        return str((self.player.name, self.x, self.y))


class Env(object):
    def __init__(self) -> None:
        self.board: Board = np.full((8, 8), Player.NONE, dtype="object")
        self.stack: List[Board] = []

    def reset(self) -> Tuple[Player, npt.NDArray]:
        self.board[3, 3] = Player.BLACK
        self.board[4, 3] = Player.WHITE
        self.board[3, 4] = Player.WHITE
        self.board[4, 4] = Player.BLACK
        return Player.BLACK, self.board

    def gameset(self) -> bool:
        black_moves = self.legal_moves(Player.BLACK)
        if len(black_moves) != 0:
            return False

        white_moves = self.legal_moves(Player.WHITE)
        if len(white_moves) != 0:
            return False

        return True

    def undo(self) -> None:
        self.board = self.stack.pop()

    def step(self, move: Move) -> Tuple[Player, npt.NDArray]:
        """Update othello board by a move"""
        if move.is_pass():
            return move.player.next(), self.board

        assert self._is_legal_move(move), "specified move is illegal!"

        # Store previous state
        self.stack.append(self.board.copy())

        # Put an othello disk
        player = move.player
        x, y = move.x, move.y
        self.board[x, y] = player

        # Turn over another player's disks
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and self.board[nx, ny] == player.next():
                nx += dx
                ny += dy
                if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
                    while self.board[nx, ny] == player.next():
                        nx += dx
                        ny += dy
                        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                            return move.player.next(), self.board

                    if self.board[nx, ny] == player:
                        while True:
                            nx -= dx
                            ny -= dy
                            if nx == x and ny == y:
                                break
                            self.board[nx, ny] = player

        return move.player.next(), self.board

    def legal_moves(self, player: Player) -> List[Move]:
        """List legal moves"""
        moves = []
        for i in range(8):
            for j in range(8):
                move = Move(player, i, j)
                if self._is_legal_move(move):
                    moves.append(move)

        return moves

    def render(self) -> npt.NDArray[np.uint8]:
        size = 1024  # size of board
        csize = size // 8  # size of cell
        margin = 10  # margin from disk to grid line

        img = Image.new("RGB", (size, size), color="#007700")
        draw = ImageDraw.Draw(img)

        # Grid lines
        for i in range(1, 8):
            y = i * csize
            draw.line((0, y, size, y), "black", width=3)

        for j in range(1, 8):
            x = j * csize
            draw.line((x, 0, x, size), "black", width=2)

        # Stars
        stars = [
            (csize * 2 - 10, csize * 2 - 10, csize * 2 + 10, csize * 2 + 10),
            (csize * 2 - 10, csize * 6 - 10, csize * 2 + 10, csize * 6 + 10),
            (csize * 6 - 10, csize * 2 - 10, csize * 6 + 10, csize * 2 + 10),
            (csize * 6 - 10, csize * 6 - 10, csize * 6 + 10, csize * 6 + 10),
        ]
        for st in stars:
            draw.ellipse(st, fill="black")

        # Disks
        for i in range(8):
            for j in range(8):
                if self.board[i, j] != Player.NONE:
                    px = j * csize + margin
                    py = i * csize + margin
                    diameter = csize - margin * 2
                    xy = (px, py, px + diameter, py + diameter)
                    fill = "black" if self.board[i, j] == Player.BLACK else "white"
                    draw.ellipse(xy, fill=fill)

        return np.array(img, dtype="uint8")

    def _is_legal_move(self, move: Move) -> bool:
        # If the spot is not empty, it's not a legal move
        player = move.player
        x, y = move.x, move.y
        if self.board[x, y] != Player.NONE:
            return False

        # Directions to check for opponent's discs
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # For each direction...
        aite = player.next()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and self.board[nx, ny] == aite:
                while True:  # Keep going in that direction
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        break

                    if self.board[nx, ny] == Player.NONE:
                        break

                    if self.board[nx, ny] == player:
                        return True

        return False

    def __repr__(self) -> str:
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

    def count(self, player: Player = Player.NONE) -> Union[int, Tuple[int, int]]:
        if player == Player.NONE:
            return np.sum(self.board == Player.BLACK), np.sum(self.board == Player.WHITE)
        else:
            return np.sum(self.board == player)

    def __dir__(self) -> List[str]:
        return [
            "reset",
            "step",
            "undo",
            "legal_moves",
            "render",
            "count",
        ]

    def _repr_png_(self):
        fig, ax = plt.subplots()
        ax.imshow(self.render())
        ax.set(xticks=[], yticks=[])
        data = print_figure(fig, "png")
        plt.close(fig)
        return data
