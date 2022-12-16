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

import pygame

from constants import CELL_SIZE as size, KING_SYMBOL, GREY, OUTER_OUTLINE as o_line, INNER_OUTLINE as i_line

class CheckerPiece:

    def __init__(self, row_position, column_position, color_of_piece):
        self.column_position = column_position
        self.row_position = row_position
        self.color_of_piece = color_of_piece
        self.x_position = 0
        self.y_position = 0
        self.is_king = False
        self.get_pos()

    def get_pos(self):
        self.y_position = (size * self.row_position) + size // 2
        self.x_position = (size * self.column_position) + size // 2

    def make_king(self):
        self.is_king = True

    def move(self, row_pos, column_pos):
        self.row_position = row_pos
        self.column_position = column_pos
        self.get_pos()

    def draw(self, win):
        r = size//2 - o_line
        pygame.draw.circle(win, GREY, (self.x_position, self.y_position), r + i_line)
        pygame.draw.circle(win, self.color_of_piece, (self.x_position, self.y_position), r)
        
        if self.is_king:
            win.blit(KING_SYMBOL, (self.x_position - KING_SYMBOL.get_width()//2, self.y_position - KING_SYMBOL.get_height()//2))
