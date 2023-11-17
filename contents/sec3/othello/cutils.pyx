cimport cython
from cython.parallel import prange, parallel
cimport numpy as cnp


cdef enum PlayerType:
    NONE = 0
    BLACK = 1
    WHITE = -1

@cython.boundscheck(False)
@cython.wraparound(False)
def cython_is_legal_move(int player, int x, int y, cnp.ndarray[int, ndim=2] board) -> bool:
    cdef int oppo = player * -1
    cdef int i, nx, ny, dx, dy
    cdef int[8][2] directions = [
        [0, 1], [1, 0], [0, -1], [-1, 0],
        [1, 1], [-1, -1], [1, -1], [-1, 1],
    ]

    # If the spot is not empty, it's not a legal move
    if board[x, y] != NONE:
        return False

    # For each direction...
    for i in range(8):
        dx = directions[i][0]
        dy = directions[i][1]
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and board[nx, ny] == oppo:
            while True:  # Keep going in that direction
                nx, ny = nx + dx, ny + dy
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    break

                if board[nx, ny] == NONE:
                    break

                if board[nx, ny] == player:
                    return True

    return False

@cython.boundscheck(False)
@cython.wraparound(False)
def cython_step(int player, int x, int y, cnp.ndarray[int, ndim=2] board) -> None:
    cdef int oppo = player * -1
    cdef int i, nx, ny, dx, dy
    cdef int[8][2] directions = [
        [0, 1], [1, 0], [0, -1], [-1, 0],
        [1, 1], [-1, -1], [1, -1], [-1, 1],
    ]

    # Put an othello disk
    board[x, y] = player

    # Turn over another player's disks
    for i in range(8):
        dx = directions[i][0]
        dy = directions[i][1]
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx, ny] == oppo:
            nx += dx
            ny += dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                while board[nx, ny] == oppo:
                    nx += dx
                    ny += dy
                    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                        break

                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx, ny] == player:
                    while True:
                        nx -= dx
                        ny -= dy
                        if nx == x and ny == y:
                            break

                        board[nx, ny] = player
