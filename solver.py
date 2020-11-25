import numpy as np

puzzle = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
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

    # Floor division to determine which Suduko box we are in
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3

    # Check to see if box is valid
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[box_y + i][box_x + j] == number:
                return False

    # Return True if row, column, and box checks pass
    return True


# Check to see if grid is solved
def completed(grid):
    count = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                count = count + 1

    if count == 0:
        return True
    else:
        return False


def solve(grid):

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
                        solve(grid)

                        # Check if solved
                        if completed(grid):
                            return

                        # Backtracking
                        grid[y][x] = 0

                return

    return grid

