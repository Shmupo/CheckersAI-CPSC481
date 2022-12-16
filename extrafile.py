from math import inf
from time import time
from copy import deepcopy

def minmax_alpha_beta(position, depth, max_player,game):
    if depth == 0 or game.check_win():
        return position
    
    if max_player:
        best_move = None
        alpha = -inf
        for move in get_all_pieces(position, game):
            new_state = get_move(position, move)
            eval = minmax_alpha_beta(new_state, depth - 1,False,game)[0]
            print(f"Type of alpha is {type(alpha)} and type of val is {type(eval)}")
            best_move = max(best_move, new_state)
            val = max(alpha, eval)
            if val <= alpha:
                best_move = move
        return best_move
    else:
        best_move = None
        beta = inf
        for move in get_all_pieces(position,game):
            new_state = get_move(position, move)
            eval = minmax_alpha_beta(new_state, depth - 1,True, game)[0]
            best_move = min(best_move, new_state)
            val = min(beta, eval)
            if beta <= val:
                best_move = move
        return best_move

def print_board(self):
        print('---Game Board---')
        for row in self.game_board:
            for element in row:
                print(element, end ='')
            print()
        print('----------------')

def get_move(piece,move,tempBoard):
    tempBoard.make_move(piece, move,tempBoard)
    return tempBoard


def get_all_moves(board,color,game):
    moves = []
    all_color_pieces = get_all_pieces(game,color)
    for piece, ithMove in all_color_pieces.items():
        for currMove in ithMove:
            temp_board = deepcopy(game)
            temp_piece = temp_board.get_piece(piece[0],piece[1])
            new_board = get_move(temp_piece,currMove,temp_board)
            print(f"Temp piece {type(temp_piece)} and new_board {type(new_board)}")
            moves.append(new_board)
    return moves
    

def get_piece(board,row,col):
    return board.game_board[row][col]

def get_all_pieces(board, color):
    valid_moves = {}
    for y, row in enumerate(board):
        for x, element in enumerate(row):
            piece = (y, x)
            if element == color:
                valid_moves[piece] = board.moves_of_piece(piece)
    print(valid_moves)
    return valid_moves

