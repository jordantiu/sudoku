import numpy as np

# TODO: Pick Empty
# TODO: Try all numbers
# TODO: Find one that works
# TODO: Repeat
# TODO: Backtrack if you find an invalid solution


grid = [
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

# grid = [
#     [1, 0, 0, 0, 4, 9, 6, 0, 8],
#     [0, 4, 0, 8, 0, 0, 2, 0, 5],
#     [2, 9, 8, 7, 0, 0, 0, 0, 0],
#     [8, 6, 0, 9, 0, 0, 0, 0, 0],
#     [0, 5, 4, 0, 0, 0, 7, 2, 0],
#     [0, 0, 0, 0, 0, 2, 0, 8, 4],
#     [0, 0, 0, 0, 0, 7, 4, 5, 2],
#     [4, 0, 3, 0, 0, 5, 0, 1, 0],
#     [5, 0, 9, 4, 1, 0, 0, 0, 7]
#
# ]


def get_square():
    for i in range(0, 9):

        for j in range(0, 9):
            print(grid[i][j])


# get_square()
#
# print(np.matrix(grid))


# def check_empty(grid):
#     for i in range(0, 9):
#         for j in range(0, 9):
#             if grid[i][j] == 0:
#                 return (i, j)  # row, column
#
#
# def valid(grid, num, position):
#     # Check valid row
#     # for i in range(0, 9):
#     #     if grid[]
#     #
#     #
#     # # Check valid column
#     # # Check valid "Sudoku Square"
#     #
#     # # Integer Division
#     # box_x = (pos[1] // 3) * 3
#     # box_y = (pos[0] // 3) * 3
#
#


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


def solve():
    global grid

    for y in range(0, 9):
        for x in range(0, 9):
            # Check if the grid is empty with '0'
            if grid[y][x] == 0:
                # For number choices between 1 and 9
                for n in range(1, 10):
                    # if valid
                    if check_valid(y, x, n):
                        grid[y][x] = n

                        # Recursive call to find next empty square
                        solve()

                        # Backtracking
                        grid[y][x] = 0

                return
    print(np.matrix(grid))


solve()
