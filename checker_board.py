import pygame
from constants import NUM_OF_ROWS, NUM_OF_COLUMNS
from constants import RED, BLACK, WHITE
from constants import CELL_SIZE
from checker_piece import CheckerPiece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(NUM_OF_ROWS):
            for col in range(row % 2, NUM_OF_COLUMNS, 2):
                pygame.draw.rect(win, BLACK, (row*CELL_SIZE, col *CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color_of_piece == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row_position][piece.column_position], self.board[row][col] = self.board[row][col], self.board[piece.row_position][piece.column_position]
        piece.move(row, col)

        if row == 7 or row == 0:
            piece.make_king()
            if piece.color_of_piece == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(NUM_OF_ROWS):
            self.board.append([])
            for col in range(NUM_OF_COLUMNS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(CheckerPiece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(CheckerPiece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(NUM_OF_ROWS):
            for col in range(NUM_OF_COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row_position][piece.column_position] = 0
            if piece != 0:
                if piece.color_of_piece == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.column_position - 1
        right = piece.column_position + 1
        row = piece.row_position

        if piece.color_of_piece == RED or piece.is_king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color_of_piece, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color_of_piece, right))
        if piece.color_of_piece == WHITE or piece.is_king:
            moves.update(self._traverse_left(row +1, min(row+3, NUM_OF_ROWS), 1, piece.color_of_piece, left))
            moves.update(self._traverse_right(row +1, min(row+3, NUM_OF_ROWS), 1, piece.color_of_piece, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, NUM_OF_ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color_of_piece == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= NUM_OF_COLUMNS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, NUM_OF_ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color_of_piece == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves