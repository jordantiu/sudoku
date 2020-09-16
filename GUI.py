import pygame

# Init pygame
pygame.init()

# Create screen with pixel height of 800 x 600
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Sudoku Puzzle")
icon = pygame.image.load('images/sudoku.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    # Gets all events
    for event in pygame.event.get():

        # Quit sudoku game
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.



    # RGB - Red, Green, Blue
    screen.fill((255, 255, 255))
    pygame.display.update()

    # if event.type.

# HANG THE PROGRAM
