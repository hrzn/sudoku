import numpy as np
from itertools import product

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
                    return full_grid
        return None
    return grid_

