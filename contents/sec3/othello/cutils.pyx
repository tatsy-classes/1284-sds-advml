from libcpp cimport bool
cimport cython
import numpy as np
cimport numpy as cnp


cdef enum CPlayer:
    NONE = 0
    BLACK = 1
    WHITE = -1


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bool cython_is_legal_move(const int player, const int x, const int y, cnp.ndarray[int, ndim=2] board):
    cdef int oppo = -1 * player
    cdef int i, nx, ny, dx, dy
    cdef cnp.ndarray[int, ndim=2] directions = np.array([
        [0, 1], [1, 0], [0, -1], [-1, 0],
        [1, 1], [-1, -1], [1, -1], [-1, 1],
    ], dtype="int32")

    # If the spot is not empty, it's not a legal move
    if board[x, y] != CPlayer.NONE:
        return False

    # For each direction...
    for i in range(8):
        dx = directions[i, 0]
        dy = directions[i, 1]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue

        if board[nx, ny] != oppo:
            continue

        while True:
            nx += dx
            ny += dy
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                break

            if board[nx, ny] == CPlayer.NONE:
                break

            if board[nx, ny] == player:
                return True

    return False

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void cython_step(const int player, const int x, const int y, cnp.ndarray[int, ndim=2] board):
    cdef int oppo = -1 * player
    cdef int i, nx, ny, dx, dy
    cdef bool inside
    cdef cnp.ndarray[int, ndim=2] directions = np.array([
        [0, 1], [1, 0], [0, -1], [-1, 0],
        [1, 1], [-1, -1], [1, -1], [-1, 1],
    ], dtype="int32")

    # Put an othello disk
    board[x, y] = player

    # Turn over another player's disks
    for i in range(8):
        dx = directions[i, 0]
        dy = directions[i, 1]
        nx, ny = x, y
        inside = True
        while True:
            nx += dx
            ny += dy
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                inside = False
                break

            if board[nx, ny] != oppo:
                break

        if inside and board[nx, ny] == player:
            while nx != x or ny != y:
                nx -= dx
                ny -= dy
                board[nx, ny] = player
