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
                print("Error: Duplicate found in row", i, "with duplicate", grid[i][j])
                return False
            else:
                seen_row.add(grid[i][j])

            if grid[j][i] in seen_column:
                print("Error: Duplicate found in column", i, "with duplicate", grid[j][i])
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
    if not check_valid_inputs(grid):
        return False
    if not check_duplicate(grid):
        return False
    return True


