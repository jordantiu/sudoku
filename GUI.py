import pygame

# TODO: Delete numpy when finished with testing
import numpy as np

# TODO: References
# https://pythonprogramming.net/pygame-start-menu-tutorial/?completed=/pygame-drawing-shapes-objects/
# https://www.youtube.com/watch?v=jh_m-Eytq0Q&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO&index=11&ab_channel=sentdex

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

pygame.init()

# Init pygame
display_width = 800

display_height = 570
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


def text_objects(text, font):
    text_surface = font.render(text, True, black)

    return text_surface, text_surface.get_rect()


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


# TODO: Current work position 10.04.2020
# https://www.youtube.com/watch?v=XpYz-q1lxu8&feature=emb_title
# Sudoku game


# NOTE: The game board is buffered from the top left hand corner by a square_size number of pixels
square_size = 50
column_count = 9
row_count = 9

board_width = column_count * square_size
height = row_count * square_size


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
            pygame.draw.rect(screen, light_blue, (column * square_size, row * square_size, square_size, square_size), 1)


# Draws borders in between sudoku boxes
def draw_border():
    pygame.draw.rect(screen, black, (square_size, square_size + square_size * 3, square_size * 9, square_size * 3), 1)
    pygame.draw.rect(screen, black, (square_size + square_size * 3, square_size, square_size * 3, square_size * 9), 1)
    pygame.draw.rect(screen, black, (square_size, square_size, square_size * 9, square_size * 9), 1)


# TODO: Cube function 10.04.2020
def cube(x, y):
    if x < 0 or y < 0 or x > 8 or y > 8:
        return x, y


def dummy(text, x_coordinate, y_coordinate, button_width, button_height, color, hover_color):
    # Mouse Position
    mouse = pygame.mouse.get_pos()
    print(mouse)
    click = pygame.mouse.get_pressed()
    print(click)

    # Note: mouse[0] is x coordinate of mouse; mouse[1] is y coordinate
    # Button Hover
    if x_coordinate < mouse[0] < x_coordinate + button_width and y_coordinate < mouse[1] < y_coordinate + button_height:
        pygame.draw.rect(screen, hover_color, (x_coordinate, y_coordinate, button_width, button_height))

    else:
        pygame.draw.rect(screen, color, (x_coordinate, y_coordinate, button_width, button_height))

    # Button Text
    button_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(text, button_text)
    text_rect.center = ((x_coordinate + (button_width / 2)), (y_coordinate + (button_height / 2)))
    screen.blit(text_surf, text_rect)


def start_sudoku():
    sudoku = True

    # Position coordinates (x,y)
    x = 0
    y = 0

    while sudoku:
        # Background screen color
        screen.fill(white)

        # Draw the sudoku game board
        draw_board()

        # Draw borders for sudoku board
        draw_border()

        # TODO: Current position function
        pygame.draw.rect(screen, light_blue,
                         (y * square_size + square_size, x * square_size + square_size, square_size, square_size))

        # Gets all events
        for event in pygame.event.get():

            # Quit sudoku game
            if event.type == pygame.QUIT:
                quit()

            # TODO: If click (Maybe do something where we get the mouse coordinates and do a sort of floor division?)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # Arrow key movements
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and y > 0:
                    y = y - 1
                    print(x, y)
                if event.key == pygame.K_RIGHT and y < 8:
                    y = y + 1
                    print(x, y)
                if event.key == pygame.K_DOWN and x < 8:
                    x = x + 1
                    print(x, y)
                if event.key == pygame.K_UP and x > 0:
                    x = x - 1
                    print(x, y)

            # TODO: Number input CONTINUE 10.05.2020

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    grid[x][y] = 0
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    grid[x][y] = 1
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    grid[x][y] = 2
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    grid[x][y] = 3
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    grid[x][y] = 4
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    grid[x][y] = 5
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    grid[x][y] = 6
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    grid[x][y] = 7
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    grid[x][y] = 8
                    print(np.matrix(grid))
                    continue
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    grid[x][y] = 9
                    print(np.matrix(grid))
                    continue


            # TODO: Backspace to undo number

        # cube("2", 350, 350, 100, 50, white, light_blue)

        # Update screen
        pygame.display.update()

        clock.tick(60)


def exit_game():
    pygame.quit()
    quit()


main_menu()
