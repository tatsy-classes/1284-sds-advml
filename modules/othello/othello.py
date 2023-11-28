from __future__ import annotations

import os
import enum
from typing import List, Tuple, Union
from itertools import product

import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from IPython.core.pylabtools import print_figure

from .cothello import c_step, c_legal_moves

Board = npt.NDArray[np.object_]

__all__ = ["Player", "Move", "Env", "make"]


class Player(enum.IntEnum):
    NONE = 0
    BLACK = 1
    WHITE = -1

    def next(self) -> Player:
        assert self.value != 0

        if self == Player.BLACK:
            return Player.WHITE
        else:
            return Player.BLACK

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        if self == Player.BLACK:
            return "BLACK"
        elif self == Player.WHITE:
            return "WHITE"
        else:
            return "NONE"


class Move(object):
    def __init__(self, player: Player, x: int, y: int) -> None:
        assert 0 <= x < 8 and 0 <= y < 8

        self.player = player
        self.x = x
        self.y = y

    def is_pass(self):
        return self.x < 0 and self.y < 0

    @staticmethod
    def make_pass(player: Player) -> Move:
        move = Move(player, 0, 0)
        move.x, move.y = -1, -1
        return move

    def __eq__(self, other) -> bool:
        if self.player != other.player:
            return False
        if self.x != other.x:
            return False
        return self.y == other.y

    def __repr__(self) -> str:
        assert self.player in [Player.BLACK, Player.WHITE]
        return str((self.player.name, self.x + 1, self.y + 1))


class Env(object):
    def __init__(self) -> None:
        self.player = Player.BLACK
        self.board: Board = np.full((8, 8), Player.NONE, dtype="int32")
        self.history: List[Move] = []
        self.stack: List[Board] = []

    def copy(self) -> Env:
        env = Env()
        env.player = self.player
        env.board = self.board.copy()
        return env

    def reset(self) -> None:
        self.player = Player.BLACK
        self.board[:] = Player.NONE
        self.board[3, 3] = Player.BLACK
        self.board[4, 3] = Player.WHITE
        self.board[3, 4] = Player.WHITE
        self.board[4, 4] = Player.BLACK
        self.history.clear()
        self.stack.clear()

    def is_done(self) -> bool:
        black_moves = self.legal_moves(Player.BLACK)
        if not black_moves[0].is_pass():
            return False

        white_moves = self.legal_moves(Player.WHITE)
        if not white_moves[0].is_pass():
            return False

        return True

    def count(self, player: Player) -> int:
        return np.sum(self.board == player)

    def is_win(self, player: Player) -> bool:
        return self.count(player) > self.count(player.next())

    def is_lose(self, player: Player) -> bool:
        return not self.is_win(player)

    def undo(self) -> None:
        self.player = self.player.next()
        self.history.pop()
        self.board = self.stack.pop()

    def update(self, move: Move) -> None:
        """Update othello board by a move"""
        if move.player != self.player:
            raise RuntimeError("Player in env and that in move do not match!!")

        # Store previous state
        self.history.append(move)
        self.stack.append(self.board.copy())

        self.player = self.player.next()
        if not move.is_pass():
            c_step(move.player.value, move.x, move.y, self.board)

    def legal_moves(self, player: Player = Player.NONE) -> List[Move]:
        """List legal moves"""
        if player == Player.NONE:
            player = self.player

        is_legal = c_legal_moves(player, self.board)
        moves = [Move(player, x, y) for x, y in product(range(8), range(8)) if is_legal[x, y]]

        if len(moves) == 0:
            moves = [Move.make_pass(self.player)]

        return moves

    def render(self) -> npt.NDArray[np.uint8]:
        size = 1024  # size of board
        csize = size // 8  # size of cell
        margin = 10  # margin from disk to grid line

        # Initialize board with green color
        img = Image.new("RGB", (size, size), color="#007700")
        draw = ImageDraw.Draw(img)

        # If board history exists, highlight last move
        if len(self.history) > 0:
            last_move = self.history[-1]
            i, j = last_move.x, last_move.y
            if 0 <= i < 8 and 0 <= j < 8:
                x = j * csize
                y = i * csize
                draw.rectangle((x, y, x + csize, y + csize), fill="#00aa00")

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

    def __repr__(self) -> str:
        sep = "+-" * 8 + "+" + os.linesep
        ret = ""
        ret += sep
        for i in range(self.board.shape[0]):
            ret += "|"
            for j in range(self.board.shape[1]):
                if self.board[i, j] == Player.NONE:
                    ret += " "
                elif self.board[i, j] == Player.BLACK:
                    ret += "o"
                elif self.board[i, j] == Player.WHITE:
                    ret += "x"
                ret += "|"
            ret += os.linesep
            ret += sep
        return ret

    def __dir__(self) -> List[str]:
        return [
            "copy",
            "reset",
            "update",
            "undo",
            "legal_moves",
            "render",
            "count",
        ]

    def _repr_png_(self):
        fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
        img = self.render()
        size = img.shape[0]
        csize = size // 8

        ax.imshow(img)
        ax.xaxis.tick_top()
        ax.set(
            xticks=np.arange(csize // 2, size, csize),
            yticks=np.arange(csize // 2, size, csize),
            xticklabels=np.arange(1, 9),
            yticklabels=np.arange(1, 9),
        )
        data = print_figure(fig, "png")
        plt.close(fig)
        return data


def make() -> Env:
    return Env()
