import numpy as np
from itertools import product
import time

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

game = np.array([
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

def is_array_valid(ar):
    vals = ar[ar != 0]
    return len(np.unique(vals)) == len(vals)

def is_rows_valid(grid):
    return all([is_array_valid(grid[i, :]) for i in range(9)])

def is_squares_valid(grid):
    return all([is_array_valid(grid[i*3:(i+1)*3, j*3:(j+1)*3].flat) for i, j in product(range(3), range(3))])

def is_grid_valid(grid):
    return is_rows_valid(grid) and is_rows_valid(grid.T) and is_squares_valid(grid)

def solve(grid):
    # Returns either the solved grid, or None if no solution exists
    grid_ = grid.copy()
    for i, j in product(range(9), range(9)):
        if grid_[i, j] != 0: continue
        for nr in range(1, 10):
            grid_[i, j] = nr 
            if is_grid_valid(grid_):
                full_grid = solve(grid_)
                if full_grid is not None:
                    # We found a solution, return it
                    return full_grid

        # We couldn't find any valid number for this position 
        return None

    return grid_

tic = time.time()
print(solve(game_easy))                
tac = time.time()

print('Solution found in {} ms.'.format((tac-tic)*1e3))
