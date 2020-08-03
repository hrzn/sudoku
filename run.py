from sudoku import solve
import time
import numpy as np

game_easy = np.array([
    [6, 0, 0, 5, 0, 2, 9, 0, 0],
    [2, 0, 3, 0, 9, 8, 6, 0, 0],
    [1, 8, 0, 0, 7, 0, 0, 3, 0],

    [0, 1, 0, 3, 0, 0, 0, 8, 5],
    [0, 9, 0, 0, 0, 0, 0, 7, 0],
    [4, 2, 0, 0, 0, 5, 0, 9, 0],

    [0, 4, 0, 0, 5, 0, 0, 6, 1],
    [0, 0, 7, 6, 1, 0, 8, 0, 9],
    [0, 0, 1, 8, 0, 3, 0, 0, 4]
], dtype=np.uint8)

game_hard = np.array([
    [6, 5, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 6, 0, 0],
    [9, 0, 2, 0, 7, 0, 0, 0, 8],

    [0, 6, 9, 2, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 8, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 4, 5, 2, 0],

    [8, 0, 0, 0, 5, 0, 1, 0, 2],
    [0, 0, 4, 0, 0, 0, 9, 5, 6],
    [0, 0, 0, 1, 0, 0, 0, 8, 3]
], dtype=np.uint8)

tic = time.time()
solution = solve(game_easy)
tac = time.time()

if solution is None:
    print('This grid has no solution.')
else:
    print(solution)
print('Found in {} ms.'.format((tac-tic)*1e3))
