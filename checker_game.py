#==============================================
# Filename: checker_game.py
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
# This file is responsible for running the
# game and creating the objects required
# to run the game.
#==============================================

#==============================================
# Modules
#==============================================
import pygame as pg

from constants import RED, WHITE
from constants import size
from checker_board import Board
#==============================================

#==============================================
# Class Name: Game
#==============================================
# Description:
# Generates and runs the game loop for the checkers game.
# Calls onto the AI to make moves and displays each move
# in the window.
#==============================================
class Game:
    
    #==============================================
    # Function Name: __init__
    #==============================================
    # Description: Used to initialize the game window.
    # and create the canvas of the board
    #==============================================
    # Input: self, window
    #==============================================
    # Output: Created window
    #==============================================
    def __init__(self, window):
        self._init()
        self.window = window

    #==============================================
    # Function Name: update
    #==============================================
    # Description: Redraws the board onto the screen 
    # after each move is made
    #==============================================
    # Input: self
    #==============================================
    # Output: Drew the board and all potential moves
    #==============================================
    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pg.display.update()

    #==============================================
    # Function Name: _init
    #==============================================
    # Description: This is used to reset the board 
    # when restarting a move
    #==============================================
    # Input: self
    #==============================================
    # Output: Moves have been reset
    #==============================================
    def _init(self):
        self.selected = None
        self.turn = RED
        self.valid_moves = {}
        self.board = Board()

    #==============================================
    # Function Name: _init
    #==============================================
    # Description: Resetting the board after a 
    # possible move is displayed to the player
    #==============================================
    # Input: self
    #==============================================
    # Output: Calls _init() function that resets the
    # board.
    #==============================================
    def reset(self):
        self._init()

    #==============================================
    # Function Name: move
    #==============================================
    # Description: Moves a piece on the board to a 
    # specified spot
    #==============================================
    # Input: self, row, col
    #==============================================
    # Output: Moves checker piece from row1 col1 to
    # row2 col2. (i.e., New position on the board)
    #==============================================
    def move(self, row, col):
        piece = self.board.get_piece(row, col)
        
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            passed = self.valid_moves[(row, col)]
            
            if passed:
                self.board.remove(passed)
            self.change_turn()
        else:
            return False

        return True

    #==============================================
    # Function Name: select
    #==============================================
    # Description: Player chooses a piece to move
    #==============================================
    # Input: self, row, col
    #==============================================
    # Output: PIece is highlighted. All valid moves
    # are displayed for player to choose.
    #==============================================
    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color_of_piece == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    #==============================================
    # Function Name: draw_valid_moves
    #==============================================
    # Description: Iterates through all of the valid 
    # moves generated and displays them one by one 
    # onto the screen
    #==============================================
    # Input: self, moves
    #==============================================
    # Output: Draws all valid moves by highlighted
    # the cell in red.
    #==============================================
    def draw_valid_moves(self, moves):
        for action in moves:
            row, col = action
            pg.draw.rect(self.win, RED, (col *size, row *size, size, size))

    #==============================================
    # Function Name: change_turn
    #==============================================
    # Description: If red makes move, then it is
    # white's turn. If white makes a move, then it
    # is red's turn.
    #==============================================
    # Input: self
    #==============================================
    # Output: Turn has been switched from current
    # player to the next player.
    #==============================================
    # ends current turn and passed to opponent
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    #==============================================
    # Function Name: get_board
    #==============================================
    # Description: Returns a copy of the board
    #==============================================
    # Input: self
    #==============================================
    # Output: self.board returned
    #==============================================
    # only returns the board
    def get_board(self):
        return self.board

    #==============================================
    # Function Name: ai_move
    #==============================================
    # Description: Passes the turn to AI after
    # opponent has made a turn.
    #==============================================
    # Input: self, checkers_board
    #==============================================
    # Output: Piece has changed the turn
    #==============================================
    def ai_move(self, checkers_board):
        self.board = checkers_board
        self.change_turn()

    #==============================================
    # Function Name: winner
    #==============================================
    # Description: Returns winner of the game (if any)
    #==============================================
    # Input: self
    #==============================================
    # Output: Winner of the game
    #==============================================
    # detects whether there is a winner to end the game
    def winner(self):
        return self.checkers_board.winner()
