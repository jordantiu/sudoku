import numpy as np
import random

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


def add_blanks(grid):
    limit = 5
    for i in range(0, 9):
        count = 0
        for j in range(0, 9):
            x = random.randint(0, 1)
            if x == 1 and count != limit:
                grid[i][j] = 0
                count = count + 1

    return grid


# TODO: Work on verifying grid has a unique solution
def reset_grid(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            grid[i][j] = 0


count = 0
is_unique = True

def check_if_unique(grid):
    global count
    global is_unique

    if is_unique == False:
        return False

    for y in range(0, 9):
        for x in range(0, 9):
            # Check if the grid is empty with '0'
            if grid[y][x] == 0:
                # For number choices between 1 and 9
                for n in range(1, 10):
                    # if valid
                    if check_valid(y, x, n, grid):
                        grid[y][x] = n

                        # Recursive call to find next empty square
                        check_if_unique(grid)

                        # # Check if solved
                        # if completed(grid):
                        #     return

                        # Backtracking
                        grid[y][x] = 0

                return

    count = count + 1

    if count > 1:
        is_unique = False

    return

# fill(blank)
# add_blanks(blank)
# print(np.matrix(blank))
# check_if_unique(blank)
# print(is_unique)


def generate_unique_puzzle(grid):
    global is_unique
    global count

    building_sudoku = True

    while building_sudoku:
        fill(grid)
        add_blanks(grid)
        check_if_unique(grid)

        if is_unique:
            building_sudoku = False

        else:
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

            is_unique = True
            count = 0

    return grid


generate_unique_puzzle(blank)
