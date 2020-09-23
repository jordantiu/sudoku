import numpy as np
import random

from validate import check_grid

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def check_valid(y, x, number):
    global grid

    # Check if row is valid
    for i in range(0, 9):
        if grid[y][i] == number:
            return False

    # Check if column is valid
    for i in range(0, 9):
        if grid[i][x] == number:
            return False

    # Floor division to determine which Sudoko box we are in
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3

    # Check to see if box is valid
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[box_y + i][box_x + j] == number:
                return False

    # Return True if row, column, and box checks pass
    return True


def fill():
    global grid

    for y in range(0, 9):
        for x in range(0, 9):
            # Check if the grid is empty with '0'
            if grid[y][x] == 0:
                # For number choices between 1 and 9
                for z in range(1, 9):
                    choices_left = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                    n = random.choice(tuple(choices_left))
                    choices_left.remove(n)

                    # if valid
                    if check_valid(y, x, n):
                        grid[y][x] = n

                        # Recursive call to find next empty square
                        fill()

                        # End random grid generation
                        if grid[8][8] != 0:
                            return

                        # Revert number to zero when backtracking
                        grid[y][x] = 0

                return


fill()

print(np.matrix(grid))

print(check_grid(grid))