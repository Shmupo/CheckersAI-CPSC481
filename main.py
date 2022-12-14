# TODO
# jumps, aka way to eliminate pieces
# some move verification on the player side
# executing moves
# what to do when checkers piece reaches the end of the other side?
# somehow allow piece to jump backwards to eliminate opponents
# allow chaining of jumps
# entire AI not done
from __future__ import print_function
from copy import deepcopy

class Checkers:
    game_board = [['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #0
                  ['B', '_', 'B', '_', 'B', '_', 'B', '_'],#1
                  ['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #2
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #3
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #4
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_'], #5
                  ['_', 'W', '_', 'W', '_', 'W', '_', 'W'], #6
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_']] #7

    def __init__(self, player, player2):
        # stores all of the current moves of each piece on the board
        self.white_moves = {}
        self.black_moves = {}
        self.running = True
        self.player1 = player
        self.player2 = player2
        self.current_turn = 'W'

    # pos : (y, x)
    # returns open position in direction
    # if an opponent piece is in the space ahead, tries to return the spot over that opponent piece 
    def returnMoves(self, color):
        if color =="W": 
            return self.white_moves
        else: 
            return self.black_moves
    def down_right(self, pos):
        if pos[0] < 7 and pos[1] < 7:
            if self.game_board[pos[0] + 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] + 1)
            elif self.game_board[pos[0] + 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] < 6:
                    if self.game_board[pos[0] + 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] + 2)
                else: return None
        else: return None

    def down_left(self, pos):
        if pos[0] < 7 and pos[1] > 0:
            if self.game_board[pos[0] + 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] + 1)
            elif self.game_board[pos[0] + 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] > 1:
                    if self.game_board[pos[0] + 2][pos[1] - 2] == '_':
                        return (pos[1] - 2, pos[0] + 2)
                else: return None
        else: return None

    def up_right(self, pos):
        if pos[0] > 0 and pos[1] < 7:
            if self.game_board[pos[0] - 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] < 6:
                    if self.game_board[pos[0] - 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] - 2)
                else: return None
        else: return None

    def up_left(self, pos):
        if pos[0] > 0 and pos[1] > 0:
            if self.game_board[pos[0] - 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] > 1:
                    if self.game_board[pos[0] - 2][pos[1] - 2] == '_':
                        return (pos[0] - 2, pos[1] - 2, )
                else: return None
        else: return None

    def print_board(self):
        print('---Game Board---')
        for row in self.game_board:
            for element in row:
                print(element, end ='')
            print()
        print('----------------')

    def print_moves(self, color):
        if color == 'W': 
            moves_list = self.white_moves
        else: 
            moves_list = self.black_moves
        print('Available moves : ')
        for x, y in moves_list.keys():
            print('Piece : (', y, x, ')', end=' | ')
            print(f'Moves : {moves_list[(x, y)]}')

    # returns the valid moves at a position (y, x)
    def moves_of_piece(self, pos):
        moves = []
        if self.game_board[pos[0]][pos[1]] == 'B':
            DR = self.down_right(pos)
            DL = self.down_left(pos)
            if DR != None: moves.append(DR)
            if DL != None: moves.append(DL)

        elif self.game_board[pos[0]][pos[1]] == 'W':
            UR = self.up_right(pos)
            UL = self.up_left(pos)
            if UR != None: moves.append(UR)
            if UL != None: moves.append(UL)
        return moves

    # returns a list of the positions of pieces of a certain color that can move
    # color is either 'W' or 'B'
    def update_moves(self):
        for y, row in enumerate(self.game_board):
            for x, element in enumerate(row):
                piece = (y, x)
                if element == 'B':
                    self.black_moves[piece] = self.moves_of_piece(piece)
                elif element == 'W':
                    self.white_moves[piece] = self.moves_of_piece(piece)
                elif element == '_':
                    #if piece in self.white_moves: del self.white_moves[y, x]
                    #if piece in self.black_moves: del self.black_moves[y, x]
                    pass

    # return true if move is valid
    def try_move(self, piece, move, color):
        if color == 'W' : move_list = self.white_moves
        elif color == 'B' : move_list = self.black_moves

        if piece in move_list:
            if move in move_list[piece]: return True
            else: return False
        else: return False

    # executes a move
    def make_move(self, piece, move, color):
        if self.try_move(piece, move, color):
            self.game_board[move[1]][move[0]] = color
            self.game_board[piece[0]][piece[1]] = '_'
            return True
        else:
            print('Invalid, try again...')
            return False

    # returns True if game is won
    def check_win(self):
        color = None
        for row in self.game.board:
            for element in row:
                if element != 0 and color == None: 
                    color = element
                elif color != None and color != element: 
                    return False

    # call this to start the game loop





# mostly handles input from player
class CheckersPlayer:
    def __init__(self, player_name, color):
        self.name = player_name
        self.color = color
        self.current_turn = 'B'

    # prompt player to select piece
    def get_piece(self):
        while True:
            pos = input('Enter the position, x,y of a piece to move : ')
            try:
                pos = pos.split(",")
                output = (int(pos[0]), int(pos[1]))
                return output
            except:
                print('Invalid input, try again.')

    # prompt player to select square to move to
    def get_move(self):
        while True:
            pos = input('Enter the position, x,y of a square to move to : ')
            try:
                pos = pos.split(",")
                output = (int(pos[0]), int(pos[1]))
                return output
            except:
                print('Invalid input, try again.')


class CheckersAI():
    def minmax(self, board, depth, max_player,checkers): # sees what the best move is to make
        if depth == 0:
            return checkers.check_win(), board
        
        if max_player:
            alpha = float('-inf')
            for move in self.getAllMoves(board,"B",checkers):
                val = self.minmax(move, depth-1, False, board)[0]
                alpha = max(alpha, val)
                if alpha == beta:
                        best_move = val
            return alpha, best_move
        else: 
            beta = float('+inf')
            for move in self.getAllMoves(board,"W",checkers):
                val = self.minmax(move, depth-1, True , board)[0]
                beta = min(beta, val)
                if beta == val:
                        best_move = val
            return beta,best_move
    # self.white_moves = {currPosition : [[moveOne],[moveTwo]]}
    
    def get_move(self, pos,piece, board,checkers):
        checkers.move([pos[1]][pos[0]])
        board[piece[0]][piece[1]] = '_'
        return board
    

    def getAllMoves(self,board,color,checkers):
        moves = []
        checkPieces = None
        currValidMoves = None
        checkPieces = self.get_color_moves(color,board,checkers)
        
        for currPos, possibleMoves in checkPieces.items():
            currValidMoves = possibleMoves
            for i in currValidMoves:
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(currPos[0],currPos[1])
                new_board = self.get_move(temp_piece,i,temp_board,checkers)
                moves.append([new_board,currPos])
        return moves

    
    def moves_of_piece(self, pos,board,color,checkers):
        moves = []
        if board[pos[0]][pos[1]] == color:
            DR = checkers.down_right(pos)
            DL = checkers.down_left(pos)
            if DR != None: 
                moves.append(DR)
            if DL != None: 
                moves.append(DL)
        return moves

    # returns a list of the positions of pieces of a certain color that can move
    # color is either 'W' or 'B'
    def get_color_moves(self,color,board,checkers):
        movesHash = {}
        for y, row in enumerate(board):
            for x, element in enumerate(row):
                piece = (y, x)
                if element == color:
                    movesHash[piece] = self.moves_of_piece(piece,board,color,checkers)
        return movesHash


def main():
    player1 = CheckersPlayer('Human', 'W')
    player2 = CheckersAI()
    checkers = Checkers(player1, player2)
    while checkers.running:
        checkers.print_board()
        checkers.update_moves()
        checkers.print_moves(checkers.current_turn)
        
        #white player turn
        if checkers.current_turn == 'W':
            valid_move = False
            while not valid_move:
                pos = checkers.player1.get_piece()
                pos = (pos[1], pos[0])
                print(pos, ' selected.')
                to_pos = checkers.player1.get_move()
            
                valid_move = checkers.make_move(pos, to_pos, checkers.player1.color)
            print('Moved ', pos, 'to', to_pos)
            input('Press enter to end turn...')
        
        print("This is the AI possible moves : ")
        checkers.print_moves("B")
        value, bestMove = checkers.player2.minmax(checkers.game_board,3,True,Checkers)
        checkers.game_board = bestMove
        print(f"The best position the AI could make is moving from position{pos} over to position{to_pos}")
        checkers.current_turn = "W"
        

if __name__ == '__main__':
    main()
