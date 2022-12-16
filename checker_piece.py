#==============================================
# Filename: checker_piece.py
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
# This file is responsible for creating checker
# piece objects on the board.
#==============================================

#==============================================
# Modules
#==============================================
import pygame

from constants import CELL_SIZE as size, KING_SYMBOL, GREY, OUTER_OUTLINE as o_line, INNER_OUTLINE as i_line
#==============================================

#==============================================
# Class Name: CheckerPiece
#==============================================
# Description:
# This class is responsibe for all functions
# for each individual checkers piece.
#==============================================
class CheckerPiece:

    #==============================================
    # Function Name: __init__
    #==============================================
    # Description: Used to initialize each checkers
    # piece by initializing position, king status,
    # and color.
    #==============================================
    # Input: self, row_position, column_position, color_of_piece
    #==============================================
    # Output: Initialized checkers piece.
    #==============================================
    def __init__(self, row_position, column_position, color_of_piece):
        self.column_position = column_position
        self.row_position = row_position
        self.color_of_piece = color_of_piece
        self.x_position = 0
        self.y_position = 0
        self.is_king = False
        self.get_pos()

    #==============================================
    # Function Name: get_pos
    #==============================================
    # Description: Retrieves current position of
    # checkers piece.
    #==============================================
    # Input: self
    #==============================================
    # Output: Checker piece returned.
    #==============================================
    def get_pos(self):
        self.y_position = (size * self.row_position) + size // 2
        self.x_position = (size * self.column_position) + size // 2

    #==============================================
    # Function Name: make_king
    #==============================================
    # Description: Sets the checkers piece to king
    # status
    #==============================================
    # Input: self
    #==============================================
    # Output: is_king is now true
    #==============================================
    def make_king(self):
        self.is_king = True

    #==============================================
    # Function Name: move
    #==============================================
    # Description: Moves checker piece to new x and
    # y coordinate.
    #==============================================
    # Input: self, row_pos, column_pos
    #==============================================
    # Output: Checker piece has been moved.
    #==============================================
    def move(self, row_pos, column_pos):
        self.row_position = row_pos
        self.column_position = column_pos
        self.get_pos()

    #==============================================
    # Function Name: move
    #==============================================
    # Description: Draws checker piece in each
    # iteration. If it is a king, then king image
    # is placed on the checkers piece.
    #==============================================
    # Input: self, win
    #==============================================
    # Output: Checker piece has been drawn.
    #==============================================
    def draw(self, win):
        
        # Radius
        r = size//2 - o_line
        
        # Outline of chess piece
        pygame.draw.circle(win, GREY, (self.x_position, self.y_position), r + i_line)
        
        # Outline of inner piece
        pygame.draw.circle(win, self.color_of_piece, (self.x_position, self.y_position), r)
        
        if self.is_king:
            # If king, then add king image.
            win.blit(KING_SYMBOL, (self.x_position - KING_SYMBOL.get_width()//2, self.y_position - KING_SYMBOL.get_height()//2))
