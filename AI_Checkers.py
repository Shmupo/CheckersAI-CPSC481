class Checkers:
    game_board = [[0, 'B', 0, 'B', 0, 'B', 0, 'B'], #0
                  ['B', 0, 'B', 0, 'B', 0, 'B', 0], #1
                  [0, 'B', 0, 'B', 0, 'B', 0, 'B'], #2
                  [0,  0,  0,  0,  0,  0,  0,  0], #3
                  [0,  0,  0,  0,  0,  0,  0,  0], #4
                  ['W', 0, 'W', 0, 'W', 0, 'W', 0], #5
                  [0, 'W', 0, 'W', 0, 'W', 0, 'W'], #6
                  ['W', 0, 'W', 0, 'W', 0, 'W', 0]] #7

    def __init__(self):
        self.pieces = []
        self.turn = 'B'

    # pos : (y, x)
    # returns open position in direction
    # if an opponent piece is in the space ahead, tries to return the spot over that opponent piece 
    def down_right(self, pos):
        if pos[0] < 7 and pos[1] < 7:
            if self.game_board[pos[0] + 1][pos[1] + 1] == 0:
                return (pos[0] + 1, pos[1] + 1)
            else:
                if pos[0] < 6 and pos[1] < 6:
                    if self.game_board[pos[0] + 2][pos[1] + 2] == 0:
                        return (pos[0] + 2, pos[1] + 2)
                else: return None
        else: return None

    def down_left(self, pos):
        if pos[0] < 7 and pos[1] > 0:
            if self.game_board[pos[0] + 1][pos[1] - 1] == 0:
                return (pos[0] + 1, pos[1] - 1)
            else:
                if pos[0] < 6 and pos[1] > 1:
                    if self.game_board[pos[0] + 2][pos[1] - 2] == 0:
                        return (pos[0] + 2, pos[1] - 2)
                else: return None
        else: return None

    def up_right(self, pos):
        if pos[0] > 0 and pos[1] < 7:
            if self.game_board[pos[0] - 1][pos[1] + 1] == 0:
                return (pos[0] - 1, pos[1] + 1)
            else:
                if pos[0] > 1 and pos[1] < 6:
                    if self.game_board[pos[0] - 2][pos[1] + 2] == 0:
                        return (pos[0] - 2, pos[1] + 2)
                else: return None
        else: return None

    def up_left(self, pos):
        if pos[0] > 0 and pos[1] > 0:
            if self.game_board[pos[0] - 1][pos[1] - 1] == 0:
                return (pos[0] - 1, pos[1] - 1)
            else:
                if pos[0] > 1 and pos[1] > 1:
                    if self.game_board[pos[0] - 2][pos[1] - 2] == 0:
                        return (pos[0] - 2, pos[1] - 2)
                else: return None
        else: return None


    # returns the valid moves at a position (y, x)
    def valid_moves(self, pos):
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

    # End game when there is only 1 color in play
    def check_goal(self):
        color = None
        for row in self.game.board:
            for element in row:
                if element != 0 and color == None: color = element
                elif color != None and color != element: return False
        else: return True

class CheckersAssistant:
    def __init__(self, color):
        self.color = color

    # suggests the best move to make
    def suggest_move(self, piece):
        pass

    # returns a value of how good a move is
    def est_move_value(self, move):
        pass

    # calculates the best move for a piece
    def calc_best_move(self, piece):
        pass

    # get the pieces on the board
    def get_board_pieces(self, board):
        pass