import pygame
from constants import CELL_SIZE, KING_SYMBOL, GREY, OUTER_OUTLINE, INNER_OUTLINE

class CheckerPiece:

    def __init__(self, row_position, column_position, color_of_piece):
        self.row_position = row_position
        self.column_position = column_position
        self.color_of_piece = color_of_piece
        self.is_king = False
        self.x_position = 0
        self.y_position = 0
        self.calc_pos()

    def calc_pos(self):
        self.x_position = CELL_SIZE * self.column_position + CELL_SIZE // 2
        self.y_position = CELL_SIZE * self.row_position + CELL_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = CELL_SIZE//2 - OUTER_OUTLINE
        pygame.draw.circle(win, GREY, (self.x_position, self.y_position), radius + INNER_OUTLINE)
        pygame.draw.circle(win, self.color_of_piece, (self.x_position, self.y_position), radius)
        if self.is_king:
            win.blit(KING_SYMBOL, (self.x_position - KING_SYMBOL.get_width()//2, self.y_position - KING_SYMBOL.get_height()//2))

    def move(self, row_position, column_position):
        self.row_position = row_position
        self.column_position = column_position
        self.calc_pos()