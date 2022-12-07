class Checkers:
    game_board = [['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #0
                  ['B', '_', 'B', '_', 'B', '_', 'B', '_'],#1
                  ['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #2
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #3
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #4
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_'], #5
                  ['_', 'W', '_', 'W', '_', 'W', '_', 'W'], #6
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_']] #7

    def __init__(self):
        self.turn = 'B'
        # stores all of the current moves of each piece on the board
        self.white_moves = {}
        self.black_moves = {}

    # pos : (y, x)
    # returns open position in direction
    # if an opponent piece is in the space ahead, tries to return the spot over that opponent piece 
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
                        return ( pos[1] - 2, pos[0] - 2)
                else: return None
        else: return None

    def print_board(self):
        print('---Game Board---')
        for row in self.game_board:
            for element in row:
                print(element, end=' ')
            print()
        print('----------------')

    def print_moves(self, color):
        if color == 'W': moves_list = self.white_moves
        elif color == 'B': moves_list = self.black_moves
        print('Available moves : ')
        for x, y in moves_list.keys():
            print('Piece : (', y, x, ')', end=' | ')
            print('Moves : (', moves_list[(x, y)], moves_list[(x, y)])

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

    # x_dir is either 'L' or 'R' -> left or right
    # y_dire is either 'U' or 'D' -> up or down
    # piece_pos is the position of the piece to move : (x, y)
    def try_move(self, piece_pos, x_dir, y_dir):
        pass

    # returns True if game is won
    def check_win(self):
        color = None
        for row in self.game.board:
            for element in row:
                if element != 0 and color == None: color = element
                elif color != None and color != element: return False
        else: return True


class CheckersPlayer:
    def __init__(self, player_name, color, checkers_game):
        self.name = player_name
        self.color = color
        self.checkers = checkers_game
        self.game_board = self.checkers.game_board

    def prompt_player(self):
        not_valid_piece = False
        



class CheckersAssistant(CheckersPlayer):
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


def main():
    checkers = Checkers()

    checkers.print_board()
    checkers.update_moves()
    checkers.print_moves('W')
    

if __name__ == '__main__':
    main()
