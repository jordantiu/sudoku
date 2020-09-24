import unittest
import validate


class TestValidate(unittest.TestCase):

    # Valid Sudoku grid with no duplicates in row, column and boxes
    def test_check_duplicate_correct(self):
        grid = [
            [9, 7, 5, 6, 1, 2, 3, 8, 4],
            [2, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_duplicate(grid)

        self.assertEqual(result, True)

    # Duplicate in a row
    def test_check_duplicate_row_duplicate(self):
        grid = [
            [9, 9, 5, 6, 1, 2, 3, 8, 4],
            [2, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_duplicate(grid)

        self.assertEqual(result, False)

    # Duplicate in a column
    def test_check_duplicate_column_duplicate(self):
        grid = [
            [9, 7, 5, 6, 1, 2, 3, 8, 4],
            [9, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_duplicate(grid)

        self.assertEqual(result, False)

    # Duplicate in a box (with columns and rows having no duplicate)
    def test_check_duplicate_box_duplicate(self):
        grid = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]

        result = validate.check_duplicate(grid)

        self.assertEqual(result, False)

    # Invalid input of -1
    def test_check_valid_inputs_1(self):
        grid = [
            [-1, 7, 5, 6, 1, 2, 3, 8, 4],
            [2, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_valid_inputs(grid)

        self.assertEqual(result, False)

    # Invalid input of 10
    def test_check_valid_inputs_2(self):
        grid = [
            [10, 7, 5, 6, 1, 2, 3, 8, 4],
            [2, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_valid_inputs(grid)

        self.assertEqual(result, False)

    # Test for check_grid
    def test_check_grid(self):
        grid = [
            [9, 7, 5, 6, 1, 2, 3, 8, 4],
            [2, 4, 1, 8, 3, 5, 7, 9, 6],
            [6, 8, 3, 9, 4, 7, 5, 1, 2],
            [4, 5, 9, 3, 7, 1, 6, 2, 8],
            [1, 3, 6, 2, 8, 9, 4, 5, 7],
            [7, 2, 8, 5, 6, 4, 1, 3, 9],
            [8, 6, 7, 1, 9, 3, 2, 4, 5],
            [5, 1, 4, 7, 2, 8, 9, 6, 3],
            [3, 9, 2, 4, 5, 6, 8, 7, 1],
        ]

        result = validate.check_grid(grid)

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
