import numpy as np
import random

from validate import check_grid

puzzle = [
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [9, 6, 5, 3, 2, 7, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 4, 6, 8, 2, 7, 1],
    [4, 7, 2, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 5],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 9, 6, 8, 2, 3],
    [2, 3, 9, 8, 4, 1, 5, 6, 7]
]


# NOTE: CAN SWAP ROWS AND COLUMNS WHEN INSIDE THE CONFIDES OF THEIR RESPECTIVE BOXES
# (depending on if it is row or column)

# TODO: COMPLETED: Row Swap function
# TODO: Add column swap to master swap function

def swap(grid):
    # Change the number of potential iterations here
    random_iteration = random.randint(25, 50)

    for i in range(0, random_iteration):
        row_swap_key = random.randint(0, 8)
        column_swap_key = random.randint(0, 8)

        # Swap a random row
        # Swap Rows 0 and 1
        if row_swap_key == 0:
            grid[0], grid[1] = grid[1], grid[0]
        # Swap Rows 0 and 2
        elif row_swap_key == 1:
            grid[0], grid[2] = grid[2], grid[0]
        # Swap Rows 1 and 2
        elif row_swap_key == 2:
            grid[0], grid[1] = grid[1], grid[0]
        # Swap Rows 3 and 4
        elif row_swap_key == 3:
            grid[3], grid[4] = grid[4], grid[3]
        # Swap Rows 3 and 5
        elif row_swap_key == 4:
            grid[3], grid[5] = grid[5], grid[3]
        # Swap Rows 4 and 5
        elif row_swap_key == 5:
            grid[4], grid[5] = grid[5], grid[4]
        # Swap Rows 6 and 7
        elif row_swap_key == 6:
            grid[6], grid[7] = grid[7], grid[6]
        # Swap Rows 6 and 8
        elif row_swap_key == 7:
            grid[6], grid[8] = grid[8], grid[6]
        # Swap Rows 7 and 8
        elif row_swap_key == 8:
            grid[7], grid[8] = grid[8], grid[7]

        # Swap a random column
        # TODO: Add your column swap function here
        # Swap Columns 0 and 1
        if column_swap_key == 0:
            print("Add your functions in between")
        # Swap Columns 0 and 2
        if column_swap_key == 1:
            print("Add your functions in between")
        # Swap Columns 1 and 2
        if column_swap_key == 2:
            print("Add your functions in between")
        # Swap Columns 3 and 4
        if column_swap_key == 3:
            print("Add your functions in between")
        # Swap Columns 3 and 5
        if column_swap_key == 4:
            print("Add your functions in between")
        # Swap Columns 4 and 5
        if column_swap_key == 5:
            print("Add your functions in between")
        # Swap Columns 6 and 7
        if column_swap_key == 6:
            print("Add your functions in between")
        # Swap Columns 6 and 8
        if column_swap_key == 7:
            print("Add your functions in between")
        # Swap Columns 7 and 8
        if column_swap_key == 0:
            print("Add your functions in between")



    print(np.matrix(grid))
    print(check_grid(grid))


# TODO: Build a preliminary column swap function then merge it into the master swap function
def swap_columns(grid):
    random_iteration = random.randint(0, 50)

    for i in range(0, random_iteration):
        random_swap_key = random.randint(0, 8)

        # Swap Columns 0 and 1
        print("Add your functions in between")
        # Swap Columns 0 and 2
        # Swap Columns 1 and 2

        # Swap Columns 3 and 4
        # Swap Columns 3 and 5
        # Swap Columns 4 and 5

        # Swap Columns 6 and 7
        # Swap Columns 6 and 8
        # Swap Columns 7 and 8

def master_swap_function(grid):
    # TODO: Have your row and column swaps interchange
    print("ADD HERE")

# print(np.matrix(grid))
# print(check_grid(grid))


swap_row(puzzle)
