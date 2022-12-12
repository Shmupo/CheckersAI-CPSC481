# TODO
# implement king piece
# allow chaining of jumps
# AI player

# NOTE
# a lot of the position indexes might be mixed up, i.e. (x, y) and (y, x) are both used


from re import L


class Checkers:
    game_board = [['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #0
                  ['B', '_', 'B', '_', 'B', '_', 'B', '_'],#1
                  ['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #2
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #3
                  ['_',  '_',  '_',  '_',  '_',  'B',  '_',  '_'], #4
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_'], #5
                  ['_', 'W', '_', 'W', '_', 'W', '_', 'W'], #6
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_']] #7

    def __init__(self, player, player2):
        self.turn = 'B'
        # stores all of the current moves of each piece on the board
        self.white_moves = {}
        self.black_moves = {}
        self.running = True
        self.player1 = player
        self.player2 = player2
        self.current_turn = 'W'

    # pos : (y, x)
    # returns open position in direction
    # if an opponent piece is in the space ahead, tries to return the spot over that opponent piece, but also returns the position of the piece jumped over
    def down_right(self, pos):
        if pos[0] < 7 and pos[1] < 7:
            if self.game_board[pos[0] + 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] + 1)
            elif self.game_board[pos[0] + 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] < 6:
                    if self.game_board[pos[0] + 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] + 2, (pos[1] + 1, pos[0] + 1))
                else: return None
        else: return None

    def down_left(self, pos):
        if pos[0] < 7 and pos[1] > 0:
            if self.game_board[pos[0] + 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] + 1)
            elif self.game_board[pos[0] + 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] > 1:
                    if self.game_board[pos[0] + 2][pos[1] - 2] == '_':
                        return (pos[1] - 2, pos[0] + 2, (pos[1] - 1, pos[0] + 1))
                else: return None
        else: return None

    def up_right(self, pos):
        if pos[0] > 0 and pos[1] < 7:
            if self.game_board[pos[0] - 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] < 6:
                    if self.game_board[pos[0] - 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] - 2, (pos[1] + 1, pos[0] - 1))
                else: return None
        else: return None

    def up_left(self, pos):
        if pos[0] > 0 and pos[1] > 0:
            if self.game_board[pos[0] - 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] > 1:
                    if self.game_board[pos[0] - 2][pos[1] - 2] == '_':
                        return (pos[1] - 2, pos[0] - 2, (pos[1] - 1, pos[0] - 1))
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
            if moves_list[(x, y)] != []:
                print('Piece : (', y, x, ')', end=' | ')
                print('Moves :', end=' ')
                for move in moves_list[(x, y)]:
                    if len(move) == 3:
                        print(move[:-1], end=' ')
                    else: print(move, end=' ')
                print()

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
    # resets the 2 move lists each time this is called
    def update_moves(self):
        self.white_moves = {}
        self.black_moves = {}
        for y, row in enumerate(self.game_board):
            for x, element in enumerate(row):
                piece = (y, x)
                if element == 'B':
                    self.black_moves[piece] = self.moves_of_piece(piece)
                elif element == 'W':
                    self.white_moves[piece] = self.moves_of_piece(piece)

    # return true if move is valid
    # this is where pieces are 'captured' when jumped over
    def try_move(self, piece, move, color):
        if color == 'W' : move_list = self.white_moves
        elif color == 'B' : move_list = self.black_moves

        if piece in move_list:
            move_list = move_list[piece]
        else: return False

        for action in move_list:
            if move == action[0:2]: 
                if type(action[-1]) == tuple:
                    self.game_board[action[-1][1]][action[-1][0]] = '_'
                return True
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
                if element != 0 and color == None: color = element
                elif color != None and color != element: return False

    # call this to start the game loop
    def run(self):
        # self.player1 starts first
        player = self.player1
        while self.running:
            print('Current Turn: ', player.color)
            self.print_board()
            self.update_moves()
            self.print_moves(player.color)
            
            making_turn = True

            while making_turn == True:
                valid_move = False
                while not valid_move:
                    pos = player.get_piece()
                    pos = (pos[1], pos[0])
                    print(pos[1] ,',', pos[0], ' selected.')
                    to_pos = player.get_move()
                
                    valid_move = self.make_move(pos, to_pos, player.color)
                
                print('Move ', pos, 'to', to_pos)

                # Ending turn
                input('Press ENTER to end turn.')
                if player == self.player1: player = self.player2
                else: player = self.player1
                making_turn = False
                print()


# mostly handles input from player
class CheckersPlayer:
    def __init__(self, player_name, color):
        self.name = player_name
        self.color = color

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


class CheckersAI(CheckersPlayer):
    def __init__(self, name, color, checkers):
        super().__init__(name, color)
        self.checkers = checkers
        self.game_board = self.checkers.game_board
        self.white_moves = checkers.white_moves
        self.black_moves = checkers.black_moves

        self.action = None

    # suggests the best move to make
    def get_move(self):
        pass

    def get_piece(self):
        pass

    # returns a value of how good a move is
    def generate_tree(self):
        pass

    # calculates the best move for a piece
    def generate_move(self):
        pass


# Currently there are 2 human players
def main():
    player1 = CheckersPlayer('Human', 'W')
    player2 = CheckersPlayer('Human2', 'B')
    checkers = Checkers(player1, player2)
    
    checkers.run()
    

if __name__ == '__main__':
    main()
