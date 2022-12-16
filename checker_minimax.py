#==============================================
# Filename: checker_minimax.py
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
# This file is responsible for displaying the
# iterations of the minimax algorithm and 
# performing the minimax algorithm.
#==============================================

from copy import deepcopy
from constants import RED, WHITE
import pygame

#==============================================
# Function Name: minimax
#==============================================
# Description: minimax tree used by the A.I.
# to decide upon the best move to make.
# Calculates a value for each move and chooses
# the highest one to return.
#==============================================
# Input: Position of a piece, depth of how far
# in the tree to compute, max_player is to flag
# whether the current caller is a max_player,
# and game is the game this algorithm is 
# running in
#==============================================
# Output: The highest score and the move to make
#==============================================

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

#==============================================
# Function Name: simulate_move
#==============================================
# Description: makes a specified move onto the
# board and returns the board after the move
# was made
#==============================================
# Input: Piece to move, Move to make, Board
# to use, Game this is running in, and the move
# to not store into the current board being 
# displayed
#==============================================
# Output: The modified board after a move
# was made
#==============================================

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

#==============================================
# Function Name: get_all_moves
#==============================================
# Description: Retrieves all the valid moves
# from all the pieces of a certain color
# currently on the board
#==============================================
# Input: Board to scan, Color of pieces to pick,
# and the game this is running in.
#==============================================
# Output: A list of all moves available from
# each piece
#==============================================

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row_position, piece.column_position)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

#==============================================
# Function Name: draw_moves
#==============================================
# Description: draws the pieces onto the board
# to be displayed
#==============================================
# Input: Game this is running in, board to
# draw on, and piece to move
#==============================================
# Output: None
#==============================================

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x_position, piece.y_position), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()

