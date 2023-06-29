import os

import numpy as np


class State(object):
    def __init__(self):
        self.board = np.zeros([8, 8], dtype="int32")
        self.board[3, 3] = 1
        self.board[4, 3] = -1
        self.board[3, 4] = -1
        self.board[4, 4] = 1

    def is_finish(self) -> bool:
        return not np.any(self.board == 0)

    def __str__(self):
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
