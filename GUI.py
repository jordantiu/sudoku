import pygame
import generator
import validate
import numpy as np

# Blank Grid
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

# Lock ability to change numbers
lock = [
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

note = [
    # Squares 0 to 8
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 9 to 17
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 18 to 26
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 27 to 35
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 36 to 44
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 45 to 53
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 54 to 62
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 63 to 71
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    # Squares 72 to 80
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

duplicate = [
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

# Generate unique puzzle
generator.generate_unique_puzzle(grid)

# Record locked numbers
for i in range(0, 9):
    for j in range(0, 9):
        if grid[i][j] != 0:
            lock[i][j] = True

# Init pygame
pygame.init()

# Display dimensions
display_width = 750
display_height = 550
screen = pygame.display.set_mode((display_width, display_height))

# Game caption
pygame.display.set_caption("Sudoku Puzzle")

# Title and Icon
icon = pygame.image.load('images/sudoku.png')
pygame.display.set_icon(icon)
black = (0, 0, 0)

# Defined colors: RGB - Red, Green, Blue
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
gray = (192, 192, 192)
light_blue = (193, 225, 236)
blue = (0, 0, 255)
blue_button = (3, 169, 252)
blue_button_hover = (89, 200, 255)
duplicate_red = (255, 204, 203)
temp_number_blue = (1, 87, 155)

# Clock
clock = pygame.time.Clock()


def button(text, x_coordinate, y_coordinate, button_width, button_height, color, hover_color, action=None):
    # Mouse Position
    mouse = pygame.mouse.get_pos()
    # Click Position
    click = pygame.mouse.get_pressed()

    # Button Hover
    if x_coordinate < mouse[0] < x_coordinate + button_width and y_coordinate < mouse[1] < y_coordinate + button_height:
        pygame.draw.rect(screen, hover_color, (x_coordinate, y_coordinate, button_width, button_height))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, color, (x_coordinate, y_coordinate, button_width, button_height))

    # Button Text
    button_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(text, button_text, black)
    text_rect.center = ((x_coordinate + (button_width / 2)), (y_coordinate + (button_height / 2)))
    screen.blit(text_surf, text_rect)

    # Add black border to button
    pygame.draw.rect(screen, black, (x_coordinate, y_coordinate, button_width, button_height), 2)


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# Draws individual sudoku squares
def draw_board():
    for column in range(column_count + 1):
        # Add buffer to board
        if column == 0:
            continue
        for row in range(row_count + 1):
            # Add buffer to board
            if row == 0:
                continue
            pygame.draw.rect(screen, gray, (column * square_size, row * square_size, square_size, square_size), 1)


# Draws borders in between sudoku boxes
def draw_border():
    pygame.draw.rect(screen, black, (square_size, square_size + square_size * 3, square_size * 9, square_size * 3), 2)
    pygame.draw.rect(screen, black, (square_size + square_size * 3, square_size, square_size * 3, square_size * 9), 2)
    pygame.draw.rect(screen, black, (square_size, square_size, square_size * 9, square_size * 9), 2)


# Clears contents of a designated cube in sudoku puzzle
def color_cube(x_coordinate, y_coordinate, color):
    pygame.draw.rect(screen, color, (52 + 50 * x_coordinate, 52 + 50 * y_coordinate, 45, 45))
    # Update display
    pygame.display.update()


# Open Game Menu
def main_menu():
    menu = True

    while menu:
        # Gets all events
        for event in pygame.event.get():

            # Quit sudoku game
            if event.type == pygame.QUIT:
                menu = False

        # Screen color
        screen.fill(white)

        # Note mouse[0] is x coordinate of mouse; mouse[1] is y coordinate
        # Start button hover

        button("Start", display_width / 2 - 50, 350, 100, 50, blue_button, blue_button_hover, start_sudoku)
        button("Exit", display_width / 2 - 50, 450, 100, 50, red, bright_red, exit_game)

        # Position away from left, position away from top, button size length (increases to right), button size height (increases downward)

        # Display Game Title
        title_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("Play Sudoku", title_text, black)
        text_rect.center = ((display_width / 2), (display_height / 3))
        screen.blit(text_surf, text_rect)

        # Update screen
        pygame.display.update()


square_size = 50
column_count = 9
row_count = 9

board_width = column_count * square_size
height = row_count * square_size


def start_sudoku():
    sudoku = True

    # Position coordinates (x,y)
    x = 0
    y = 0

    # Notes
    notes_mode = False

    while sudoku:

        # Mouse position
        mouse = pygame.mouse.get_pos()

        # Background screen color
        screen.fill(white)

        # Check for duplicates
        check_duplicate()

        # Color Duplicate Squares
        for i in range(0, 9):
            for j in range(0, 9):
                if duplicate[i][j] == 1:
                    pygame.draw.rect(screen, duplicate_red,
                                     (j * square_size + square_size, i * square_size + square_size, square_size,
                                      square_size))

        # Highlight current position on board
        pygame.draw.rect(screen, light_blue,
                         (y * square_size + square_size, x * square_size + square_size, square_size, square_size))

        # Draw the sudoku game board
        draw_board()

        # Draw borders for sudoku board
        draw_border()

        # Menu Buttons
        button("New Game", 550, 50, 150, 50, blue_button, blue_button_hover)

        if not notes_mode:
            note_text = "Notes (OFF)"
        else:
            note_text = "Notes (ON)"

        # Notes
        button(note_text, 550, 150, 150, 50, blue_button, blue_button_hover)

        # Solve via backtracking algorithm
        button("Auto Solve", 550, 250, 150, 50, blue_button, blue_button_hover)

        # Exit game
        button("Exit", 550, 350, 150, 50, red, bright_red, exit_game)

        # Check if puzzle is solved
        if validate.check_grid(grid):
            # Display victory text
            button("Puzzle Solved", 550, 450, 150, 50, light_blue, light_blue)

            # Lock grid when puzzle completed
            for a in range(0, 9):
                for b in range(0, 9):
                    if grid[a][b] != 0:
                        lock[a][b] = True

            # Remove notes
            for i in range(0, 81):
                for j in range(0, 9):
                    note[i][j] = 0

        # Display numbers of the grid
        cube_text = pygame.font.Font('freesansbold.ttf', 35)
        for i in range(0, 9):
            for j in range(0, 9):
                # Make cube blank if '0'
                if grid[j][i] == 0:
                    continue

                if lock[j][i]:
                    text_surf, text_rect = text_objects(str(grid[j][i]), cube_text, black)
                    text_rect.center = (75 + i * 50, 80 + j * 50)
                    screen.blit(text_surf, text_rect)
                elif duplicate[j][i] == 1:
                    text_surf, text_rect = text_objects(str(grid[j][i]), cube_text, red)
                    text_rect.center = (75 + i * 50, 80 + j * 50)
                    screen.blit(text_surf, text_rect)
                else:
                    text_surf, text_rect = text_objects(str(grid[j][i]), cube_text, temp_number_blue)
                    text_rect.center = (75 + i * 50, 80 + j * 50)
                    screen.blit(text_surf, text_rect)

        # Display note numbers
        note_text = pygame.font.Font('freesansbold.ttf', 15)
        for i in range(0, 81):
            for j in range(0, 9):
                if note[i][j] == 0:
                    continue

                if 0 <= j <= 2:
                    text_surf, text_rect = text_objects(str(note[i][j]), note_text, black)
                    text_rect.center = (50 + 10 + j * 15 + 50 * (i % 9), 53 + 10 + 0 + 50 * (i // 9))
                    screen.blit(text_surf, text_rect)
                elif 3 <= j <= 5:
                    text_surf, text_rect = text_objects(str(note[i][j]), note_text, black)
                    text_rect.center = (50 + 10 + j % 3 * 15 + 50 * (i % 9), 53 + 10 + 15 + 50 * (i // 9))
                    screen.blit(text_surf, text_rect)
                elif 6 <= j <= 8:
                    text_surf, text_rect = text_objects(str(note[i][j]), note_text, black)
                    text_rect.center = (50 + 10 + j % 6 * 15 + 50 * (i % 9), 53 + 10 + 30 + 50 * (i // 9))
                    screen.blit(text_surf, text_rect)

        # Gets all events
        for event in pygame.event.get():

            # Quit sudoku game
            if event.type == pygame.QUIT:
                quit()

            # Generate new sudoku board on button click (unable to hold button)
            if event.type == pygame.MOUSEBUTTONDOWN and 550 < mouse[0] < 700 and 50 < mouse[1] < 100:
                new_game()

            # Generate new sudoku board on button click (unable to hold button)
            if event.type == pygame.MOUSEBUTTONDOWN and 550 < mouse[0] < 700 and 150 < mouse[1] < 200:
                if not notes_mode:
                    notes_mode = True
                else:
                    notes_mode = False

            # Solve puzzle on click
            if event.type == pygame.MOUSEBUTTONDOWN and 550 < mouse[0] < 700 and 250 < mouse[1] < 300:

                # Hide the cursor
                pygame.draw.rect(screen, white,
                                 (y * square_size + square_size, x * square_size + square_size, square_size,
                                  square_size))

                # Redraw numbers of the grid
                cube_text = pygame.font.Font('freesansbold.ttf', 35)
                for i in range(0, 9):
                    for j in range(0, 9):
                        # Make cube blank if '0'
                        if grid[j][i] == 0:
                            continue

                        if lock[j][i]:
                            text_surf, text_rect = text_objects(str(grid[j][i]), cube_text, black)
                            text_rect.center = (75 + i * 50, 80 + j * 50)
                            screen.blit(text_surf, text_rect)
                        else:
                            text_surf, text_rect = text_objects(str(grid[j][i]), cube_text, bright_red)
                            text_rect.center = (75 + i * 50, 80 + j * 50)
                            screen.blit(text_surf, text_rect)

                # Redraw the sudoku game board
                draw_board()

                # Redraw borders for sudoku board
                draw_border()

                # Reset the grid to initial puzzle
                for i in range(0, 9):
                    for j in range(0, 9):
                        if not lock[i][j]:
                            grid[i][j] = 0

                            # Make cube box white
                            color_cube(j, i, white)

                solve(grid)

            # Click to change highlighted position
            for i in range(0, 9):
                for j in range(0, 9):
                    if event.type == pygame.MOUSEBUTTONDOWN and 50 + 50 * j < mouse[0] < 100 + 50 * j and 50 + 50 * i < \
                            mouse[1] < 100 + i * 50:
                        x = i
                        y = j

                        # Formula for notes position
                        note_position = 9 * x + y

            # Arrow key movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and y > 0:
                    y = y - 1
                if event.key == pygame.K_RIGHT and y < 8:
                    y = y + 1
                if event.key == pygame.K_DOWN and x < 8:
                    x = x + 1
                if event.key == pygame.K_UP and x > 0:
                    x = x - 1

                # Formula for note position
                note_position = 9 * x + y

            # Number inputs (checks if number is locked in grid)
            if event.type == pygame.KEYDOWN and not lock[x][y] and not notes_mode:

                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    grid[x][y] = 0
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    grid[x][y] = 1
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    grid[x][y] = 2
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    grid[x][y] = 3
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    grid[x][y] = 4
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    grid[x][y] = 5
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    grid[x][y] = 6
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    grid[x][y] = 7
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    grid[x][y] = 8
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    grid[x][y] = 9
                    for i in range(0, 9):
                        note[note_position][i] = 0

            # Add notes to grid
            elif event.type == pygame.KEYDOWN and not lock[x][y] and notes_mode:

                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    grid[x][y] = 0
                    color_cube(x, y, white)
                    # Clear the notes for cube
                    for i in range(0, 9):
                        note[note_position][i] = 0
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    grid[x][y] = 0
                    note[note_position][0] = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    grid[x][y] = 0
                    note[note_position][1] = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    grid[x][y] = 0
                    note[note_position][2] = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    grid[x][y] = 0
                    note[note_position][3] = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    grid[x][y] = 0
                    note[note_position][4] = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    grid[x][y] = 0
                    note[note_position][5] = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    grid[x][y] = 0
                    note[note_position][6] = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    grid[x][y] = 0
                    note[note_position][7] = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    grid[x][y] = 0
                    note[note_position][8] = 9

        # Update screen
        pygame.display.update()

        clock.tick(60)


def exit_game():
    pygame.quit()
    quit()


# Creates new puzzle grid and answer grid
def new_game():
    # Reset grid
    for a in range(0, 9):
        for b in range(0, 9):
            grid[a][b] = 0

    # Reset notes
    for i in range(0, 81):
        for j in range(0, 9):
            note[i][j] = 0

    # Generate new grid with blanks
    generator.generate_unique_puzzle(grid)

    # Record locked numbers
    for a in range(0, 9):
        for b in range(0, 9):
            if grid[a][b] != 0:
                lock[a][b] = True
            else:
                lock[a][b] = False


def check_valid(y, x, number, puzzle):
    # Check if row is valid
    for a in range(0, 9):
        if puzzle[y][a] == number:
            return False

    # Check if column is valid
    for a in range(0, 9):
        if puzzle[a][x] == number:
            return False

    # Floor division to determine which Sudoko box we are in
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3

    # Check to see if box is valid
    for a in range(0, 3):
        for b in range(0, 3):
            if puzzle[box_y + a][box_x + b] == number:
                return False

    # Return True if row, column, and box checks pass
    return True


# Check to see if grid is solved
def completed(puzzle):
    count = 0

    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                count = count + 1

    if count == 0:
        return True
    else:
        return False


def solve(puzzle):
    cube_text = pygame.font.Font('freesansbold.ttf', 35)

    for y in range(0, 9):
        for x in range(0, 9):
            # Check if the grid is empty with '0'
            if puzzle[y][x] == 0:
                # For number choices between 1 and 9
                for n in range(1, 10):
                    # if valid
                    if check_valid(y, x, n, puzzle):
                        puzzle[y][x] = n

                        if lock[y][x]:
                            text_surf, text_rect = text_objects(str(grid[y][x]), cube_text, green)
                            text_rect.center = (75 + x * 50, 80 + y * 50)
                            screen.blit(text_surf, text_rect)
                        else:
                            text_surf, text_rect = text_objects(str(grid[y][x]), cube_text, green)
                            text_rect.center = (75 + x * 50, 80 + y * 50)
                            screen.blit(text_surf, text_rect)

                        pygame.display.update()
                        pygame.time.wait(50)

                        # Recursive call to find next empty square
                        solve(puzzle)

                        # Check if solved
                        if completed(puzzle):
                            return

                        # Backtracking
                        puzzle[y][x] = 0

                        # Make cube box white
                        color_cube(x, y, white)
                return

    return puzzle


# TODO: Create a function that will highlight duplicates that exist in a row, column, or box
def check_duplicate():
    for i in range(0, 9):
        for j in range(0, 9):
            duplicate[i][j] = 0

    print(np.matrix(duplicate))

    # Check Duplicates in Rows and Columns
    for i in range(0, 9):

        for j in range(0, 9):
            # Check for duplicates in respective row
            for column_number in range(0, 9):
                if grid[i][j] == grid[i][column_number] and j != column_number and grid[i][j] != 0:
                    duplicate[i][j] = True

            # Check for duplicates in respective column
            for row_number in range(0, 9):
                if grid[i][j] == grid[row_number][j] and i != row_number and grid[i][j] != 0:
                    duplicate[i][j] = True

            # Check for duplicates in respective box
            box_x = i // 3
            box_y = j // 3

            if box_x == 0 and box_y == 0:
                for x in range(0, 3):
                    for y in range(0, 3):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 0 and box_y == 1:
                for x in range(0, 3):
                    for y in range(3, 6):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 0 and box_y == 2:
                for x in range(0, 3):
                    for y in range(6, 9):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 1 and box_y == 0:
                for x in range(3, 6):
                    for y in range(0, 3):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 1 and box_y == 1:
                for x in range(3, 6):
                    for y in range(3, 6):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 1 and box_y == 2:
                for x in range(3, 6):
                    for y in range(6, 9):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 2 and box_y == 0:
                for x in range(6, 9):
                    for y in range(0, 3):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 2 and box_y == 1:
                for x in range(6, 9):
                    for y in range(3, 6):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True

            elif box_x == 2 and box_y == 2:
                for x in range(6, 9):
                    for y in range(6, 9):
                        if grid[i][j] == grid[x][y] and i != x and j != y and grid[i][j] != 0:
                            duplicate[i][j] = True


main_menu()
