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

import pygame as pg

from constants import RED, WHITE
from constants import size
from checker_board import Board

# Generates and runs the game loop for the checkers game.
# Calls onto the AI to make moves and displays each move
# in the window.

class Game:
    def __init__(self, window):
        self._init()
        self.window = window

    # redraws the board onto the screen after each move is made
    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pg.display.update()

    # this is used to reset the board when restarting a move
    def _init(self):
        self.selected = None
        self.turn = RED
        self.valid_moves = {}
        self.board = Board()

    # resetting the board after a possible move is displayed to the player
    def reset(self):
        self._init()

    # moves a piece on the board to a specified spot
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

    # choose a piece to move
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

    # iterates through all of the valid moves generated and displays them one by one onto the screen
    def draw_valid_moves(self, moves):
        for action in moves:
            row, col = action
            pg.draw.rect(self.win, RED, (col *size, row *size, size, size))

    # ends current turn and passed to opponent
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    # only returns the board
    def get_board(self):
        return self.board

    # passes the turn to the AI after opponent has made a turn
    def ai_move(self, checkers_board):
        self.board = checkers_board
        self.change_turn()

    # detects whether there is a winner to end the game
    def winner(self):
        return self.checkers_board.winner()