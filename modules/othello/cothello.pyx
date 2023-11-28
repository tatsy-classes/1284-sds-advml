from libcpp cimport bool
cimport cython
import numpy as np
cimport numpy as np
from cython cimport view
from cython.parallel import prange

directions_ = np.array([
    [0, 1], [1, 0], [0, -1], [-1, 0],
    [1, 1], [-1, -1], [1, -1], [-1, 1],
], dtype="int32")
cdef int[:, :] directions = directions_

cdef enum CPlayer:
    NONE = 0
    BLACK = 1
    WHITE = -1


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bool c_is_legal_move(const int player, const int x, const int y, int[:, :] board) noexcept nogil:
    cdef int other = -1 * player
    cdef int i, nx, ny, dx, dy

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

        if board[nx, ny] != other:
            continue

        while True:
            nx = nx + dx
            ny = ny + dy
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                break

            if board[nx, ny] == CPlayer.NONE:
                break

            if board[nx, ny] == player:
                return True

    return False

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef bool[:, :] c_legal_moves(const int player, int[:, :] board):
    cdef int x, y
    cdef np.ndarray[np.uint8_t, cast=True, ndim=2] is_legal = np.zeros((8, 8), dtype="uint8")
    cdef bool[:, :] view = is_legal

    for x in range(8):
        for y in range(8):
            view[x, y] = c_is_legal_move(player, x, y, board)

    return is_legal


@cython.boundscheck(False)
@cython.wraparound(False)
cpdef void c_step(const int player, const int x, const int y, int[:, :] board) noexcept nogil:
    cdef int other = -1 * player
    cdef int i, nx, ny, dx, dy
    cdef bool inside

    # Put an othello disk
    board[x, y] = player

    # Turn over another player's disks
    for i in range(8):
        dx = directions[i, 0]
        dy = directions[i, 1]
        nx, ny = x, y
        inside = True
        while True:
            nx = nx + dx
            ny = ny + dy
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                inside = False
                break

            if board[nx, ny] != other:
                break

        if inside and board[nx, ny] == player:
            while nx != x or ny != y:
                nx = nx - dx
                ny = ny - dy
                board[nx, ny] = player
