import numpy as np


# TODO: Put everything together (or encapsulate or whatever) it into a well defined class structure
# TODO: Clean up print statements in methods
# TODO: Write unit tests for methods

# Validates Sudoku puzzle by checking if sums of each of the rows, columns, and boxes is equal to 45
def check_sum(grid):
    for i in range(0, 9):
        # Validate row sum
        if sum(grid[i]) != 45:
            print("Error: Row", i, "is invalid.")
            return False
        else:
            print("Row", i, "is valid with sum of 45.")

        # Validate column Sum
        if grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i] + grid[4][i] + grid[5][i] + grid[6][i] + grid[7][i] + \
                grid[8][i] != 45:
            print("Error: Column", i, "is invalid.")
            return False
        else:
            print("Column", i, "is valid with sum of 45.")

    # Check to see if box is valid
    # Set x counter
    x = 0

    for i in range(0, 3):
        # Set/Reset y counter
        y = 0

        # Check sum of each box
        for j in range(0, 3):
            if grid[x][y] + grid[x + 1][y] + grid[x + 2][y] + \
                    grid[x][y + 1] + grid[x + 1][y + 1] + grid[x + 2][y + 1] + \
                    grid[x][y + 2] + grid[x + 1][y + 2] + grid[x + 2][y + 2] != 45:
                print("Error: Box", i, j, "is invalid.")
                return False
            else:
                print("Box", i, j, "has valid sum of 45")

            # Increment y counter
            y = y + 3

        # Increment the x counter
        x = x + 3

    return True


# Check for invalid inputs that are not between 0 and 9
def check_valid_inputs(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] > 9 or grid[i][j] < 0:
                return False
    return True


# Validates Sudoku puzzle by checking if there are any duplicates within a row, column or within a box
def check_duplicate(grid):
    # TODO: Check Duplicates in Rows and Columns
    for i in range(0, 9):
        seen_row = set()
        seen_column = set()
        for j in range(0, 9):
            if grid[i][j] in seen_row:
                print("Error: Duplicate found in row", i)
                return False
            else:
                seen_row.add(grid[i][j])

            if grid[j][i] in seen_column:
                print("Error: Duplicate found in column", i)
                return False
            else:
                seen_column.add(grid[j][i])

    # TODO: Check for duplicates in boxes
    # Check to see if box is valid
    # Set x counter
    x = 0
    # Seen square set
    seen_square = set()
    for i in range(0, 3):
        # Set/Reset y counter
        y = 0

        # Check sum of each box
        for j in range(0, 3):
            # Clear set
            seen_square.clear()

            seen_square.add(grid[x][y])
            seen_square.add(grid[x + 1][y])
            seen_square.add(grid[x + 2][y])
            seen_square.add(grid[x][y + 1])
            seen_square.add(grid[x + 1][y + 1])
            seen_square.add(grid[x + 2][y + 1])
            seen_square.add(grid[x][y + 2])
            seen_square.add(grid[x + 1][y + 2])
            seen_square.add(grid[x + 2][y + 2])

            if len(seen_square) != 9:
                print("Error: Box", i, j, "is invalid. Contains a duplicate")
                return False

            # Increment y counter
            y = y + 3

        # Increment the x counter
        x = x + 3

    return True


def check_grid(grid):
    if not check_sum(grid):
        return False
    if not check_valid_inputs(grid):
        return False
    if not check_duplicate(grid):
        return False
    return True



# TODO: Clean up this test arrays

# puzzle = [
#     [8, 2, 7, 1, 5, 4, 3, 9, 6],
#     [9, 6, 5, 3, 2, 7, 1, 4, 8],
#     [3, 4, 1, 6, 8, 9, 7, 5, 2],
#     [5, 9, 3, 4, 6, 8, 2, 7, 1],
#     [4, 7, 2, 5, 1, 3, 6, 8, 9],
#     [6, 1, 8, 9, 7, 2, 4, 3, 5],
#     [7, 8, 6, 2, 3, 5, 9, 1, 4],
#     [1, 5, 4, 7, 9, 6, 8, 2, 3],
#     [2, 3, 9, 8, 4, 1, 5, 6, 7]
# ]
#
# deviant = [
#     [1, 1, 1, 2, 2, 2, 3, 3, 3],
#     [1, 1, 1, 2, 2, 2, 3, 3, 3],
#     [1, 1, 1, 2, 2, 2, 3, 3, 3],
#     [4, 4, 4, 5, 5, 5, 6, 6, 6],
#     [4, 4, 4, 5, 5, 5, 6, 6, 6],
#     [4, 4, 4, 5, 5, 5, 6, 6, 6],
#     [7, 7, 7, 8, 8, 8, 9, 9, 9],
#     [7, 7, 7, 8, 8, 8, 9, 9, 9],
#     [7, 7, 7, 8, 8, 8, 9, 9, 9]
# ]
#
# deviant_2 = [
#     [8, 2, 7, 1, 5, 4, 3, 9, 6],
#     [9, 6, 5, 3, 2, 7, 1, 4, 8],
#     [3, 4, 1, 6, 8, 9, 7, 5, 2],
#     [5, 9, 3, 4, 6, 8, 2, 7, 1],
#     [4, 7, 2, 5, 1, 3, 6, 8, 9],
#     [6, 1, 8, 9, 7, 2, 4, 3, 5],
#     [7, 8, 6, 2, 3, 5, 9, 1, 4],
#     [1, 5, 4, 7, 9, 6, 8, 2, 3],
#     [2, 3, 9, 8, 4, 1, 5, 6, 7]
# ]
#
# print(check_grid(deviant))