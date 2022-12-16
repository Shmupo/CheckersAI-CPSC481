#==============================================
# Filename: checker_main.py
#==============================================
# Filetype: Python Source File
#==============================================
# Author(s):
#               Angaar Hamid
#               Andrew Doan
#               Alejandro Ramos
#==============================================
# Last Modified: 12/15/2022
#==============================================
# Description:
# This file is responsible for 
#==============================================

import pygame
from constants import WIDTH, HEIGHT
from constants import CELL_SIZE
from constants import RED, WHITE
from checker_game import Game
from checker_minimax import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


#==============================================
# Function Name: get_row_col_from_mouse
#==============================================
# Description: returns the the row and column 
# of a square the mouse is hovering over.
#==============================================
# Input: position of the mouse.
#==============================================
# Output: position of a square on the checkers
# board.
#==============================================
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

#==============================================
# Function Name: main
#==============================================
# Description: Initiates the checkers game and AI
# and runs the main game loop.
#==============================================
# Input: None
#==============================================
# Output: None
#==============================================

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
        if game.winner() != None:
            print(game.winner())
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        game.update()
    pygame.quit()
main()
