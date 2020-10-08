import numpy as np
import random
import validate
import solver

blank = [
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


def check_valid(y, x, number, grid):
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


def fill(grid):
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
                    if check_valid(y, x, n, grid):
                        grid[y][x] = n

                        # Recursive call to find next empty square
                        fill(grid)

                        # End random grid generation
                        if grid[8][8] != 0:
                            return

                        # Revert number to zero when backtracking
                        grid[y][x] = 0

                return
    return grid


# TODO: Write ability to generate blanks on a generated sudoku grid
# TODO: MAKE SURE YOU HAVE THE ALREADY SOLVED PUZZLE STORED (possibly needed or not?)
def add_blanks(grid):
    grid[2][2] = 0
    return grid


print(np.matrix(blank))

fill(blank)

print(np.matrix(blank))

add_blanks(blank)

print(np.matrix(blank))
