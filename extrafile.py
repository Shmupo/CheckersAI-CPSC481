from math import inf
from time import time
from copy import deepcopy

def min_max(position, depth, max_player,game):
    if depth == 0 or game.check_win():
        return position
    best_move = 0
    if max_player:
        alpha = -inf
        for move in get_all_moves(position,"B", game):
            eval = min_max(move, depth - 1,False,game)[0]
            print(eval)
            print(f"Type of alpha is {type(alpha)} and type of val is {type(eval)}")
            val = max(alpha, eval)
            #val = self.minmax(move, depth-1, True , self.checkers)[0]
            if beta == alpha:
                best_move = val
        return alpha,best_move
    else:
        beta = inf
        for move in get_all_moves(position, "W",game):
            eval = min_max(move, depth - 1,True, game)[0]
            val = min(beta, eval)
            if beta == val:
                best_move = val
        return beta,best_move

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
            moves.append([new_board,piece])
    return moves
    
#  def getAllMoves(self,board,currPos,color):
#         moves = []
#         checkPieces = None
#         currValidMoves = None
#         for currPos, possibleMoves in checkPieces.items():
#             currValidMoves = possibleMoves
#             for i in currValidMoves:
#                 temp_board = deepcopy(board)
#                 new_board = self.get_move(currPos,i,temp_board, self.checkers)
#                 moves.append([new_board,currPos])
#         return moves



def get_piece(board,row,col):
    return board.game_board[row][col]

def get_all_pieces(board, color):
    valid_moves = {}
    for y, row in enumerate(board.game_board):
        for x, element in enumerate(row):
            piece = (y, x)
            if element == color:
                valid_moves[piece] = board.moves_of_piece(piece)
    print(valid_moves)
    return valid_moves
#h
