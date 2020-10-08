import pygame

import generator
import validate
import solver

import numpy as np

# TODO: References
# https://pythonprogramming.net/pygame-start-menu-tutorial/?completed=/pygame-drawing-shapes-objects/
# https://www.youtube.com/watch?v=jh_m-Eytq0Q&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=11&ab_channel=sentdex

# Blank Grid
# grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

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

pygame.init()

# Init pygame
display_width = 750

display_height = 550
screen = pygame.display.set_mode((display_width, display_height))

# Create screen with pixel length x height of 800 x 600
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

# Clock
clock = pygame.time.Clock()


def button(text, x_coordinate, y_coordinate, button_width, button_height, color, hover_color, action=None):
    # Mouse Position
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    click = pygame.mouse.get_pressed()
    # print(click)

    # Note: mouse[0] is x coordinate of mouse; mouse[1] is y coordinate
    # Button Hover
    if x_coordinate < mouse[0] < x_coordinate + button_width and y_coordinate < mouse[1] < y_coordinate + button_height:
        pygame.draw.rect(screen, hover_color, (x_coordinate, y_coordinate, button_width, button_height))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, color, (x_coordinate, y_coordinate, button_width, button_height))

    # Button Text
    button_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(text, button_text)
    text_rect.center = ((x_coordinate + (button_width / 2)), (y_coordinate + (button_height / 2)))
    screen.blit(text_surf, text_rect)

    # Add black border to button
    pygame.draw.rect(screen, black, (x_coordinate, y_coordinate, button_width, button_height), 2)


def text_objects(text, font):
    text_surface = font.render(text, True, black)

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

        button("Start", display_width / 2 - 50, 350, 100, 50, green, bright_green, start_sudoku)
        button("Exit", display_width / 2 - 50, 450, 100, 50, red, bright_red, exit_game)

        # Position away from left, position away from top, button size length (increases to right), button size height (increases downward)

        # Display Game Title
        title_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = text_objects("Play Sudoku", title_text)
        text_rect.center = ((display_width / 2), (display_height / 3))
        screen.blit(text_surf, text_rect)

        # Update screen
        pygame.display.update()


# TODO: Current work position 10.07.2020
# https://www.youtube.com/watch?v=XpYz-q1lxu8&feature=emb_title
# Sudoku game


# NOTE: The game board is buffered from the top left hand corner by a square_size number of pixels
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

    while sudoku:

        # Mouse position
        mouse = pygame.mouse.get_pos()
        print(mouse)

        # Background screen color
        screen.fill(white)

        # Highlight current position on board
        pygame.draw.rect(screen, light_blue,
                         (y * square_size + square_size, x * square_size + square_size, square_size, square_size))

        # Draw the sudoku game board
        draw_board()

        # Draw borders for sudoku board
        draw_border()

        # TODO: Menu buttons
        button("Exit", 550, 150, 150, 50, red, white, exit_game)
        button("New Game", 550, 50, 150, 50, green, white)

        # Gets all events
        for event in pygame.event.get():

            # Quit sudoku game
            if event.type == pygame.QUIT:
                quit()

            # Generate new sudoku board on button click (unable to hold button)
            if event.type == pygame.MOUSEBUTTONDOWN and 550 < mouse[0] < 700 and 50 < mouse[1] < 100:
                new_game()

            # Click to change highlighted position
            for i in range(0, 9):
                for j in range(0, 9):
                    if event.type == pygame.MOUSEBUTTONDOWN and 50 + 50 * j < mouse[0] < 100 + 50 * j and 50 + 50 * i < \
                            mouse[1] < 100 + i * 50:
                        x = i
                        y = j

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

            # Number inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0 or event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    grid[x][y] = 0
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    grid[x][y] = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    grid[x][y] = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    grid[x][y] = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    grid[x][y] = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    grid[x][y] = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    grid[x][y] = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    grid[x][y] = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    grid[x][y] = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    grid[x][y] = 9

                # TODO: Delete Test Keys when completed with project (below)
                elif event.key == pygame.K_g:
                    print(np.matrix(grid))
                elif event.key == pygame.K_SPACE:
                    generator.fill(grid)
                elif event.key == pygame.K_n:
                    for i in range(0, 9):
                        for j in range(0, 9):
                            grid[i][j] = 0

        # Display numbers of the grid
        cube_text = pygame.font.Font('freesansbold.ttf', 35)
        for i in range(0, 9):
            for j in range(0, 9):
                # Make cube blank if '0'
                if grid[j][i] == 0:
                    continue

                text_surf, text_rect = text_objects(str(grid[j][i]), cube_text)
                text_rect.center = (75 + i * 50, 80 + j * 50)
                screen.blit(text_surf, text_rect)

        # text_surf, text_rect = text_objects(str(grid[0][0]), cube_text)
        # text_rect.center = (75, 80)
        # screen.blit(text_surf, text_rect)
        #
        # text_surf, text_rect = text_objects(str(grid[0][1]), cube_text)
        # text_rect.center = (125, 80)
        # screen.blit(text_surf, text_rect)
        #
        # text_surf, text_rect = text_objects(str(grid[1][0]), cube_text)
        # text_rect.center = (75, 130)
        # screen.blit(text_surf, text_rect)

        # TODO: Fix solver to receive input and return output

        # Update screen
        pygame.display.update()

        clock.tick(60)


def exit_game():
    pygame.quit()
    quit()


# TODO: Adjust to create a new puzzle (when fucntion is built)
# TODO: Fix the infinite click issue
def new_game():
    for i in range(0, 9):
        for j in range(0, 9):
            grid[i][j] = 0
    generator.fill(grid)


main_menu()
