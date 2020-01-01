# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 20:54:50 2019

@author: mink9
"""

from tkinter import *
        
class Sudoku_Game():
    """
    A class to represent the game and its functionalities
    
    ...
    
    Attributes
    ----------
    difficulty : str
        The difficulty of the game
    text_tracker : list
        A list to keep track of the tkinter text objects drawn on canvas
    initial_board: list
        A list to keep track of the initial state of the board
    current_board: list
        A list to keep track of the applied changes to the board
    
    Methods
    -------
    find_empty()
        Finds the next empty cell in current_board
    valid(row, col, num)
        Checks if a number is a valid move in the given cell
    check_victory()
        Checks if the current board state is complete (won)
    solve_puzzle()
        Solves the sudoku puzzle by updating the current board to reflect
        the completed board using backtracking
    """
    text_tracker = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]

    def __init__(self, difficulty):
        """
        Parameters
        ----------
        difficulty : str
            The difficulty of the game
        text_tracker : list
            A list to keep track of the tkinter text objects drawn on canvas
        initial_board: list
            A list to keep track of the initial state of the board
        current_board: list
            A list to keep track of the applied changes to the board
        """
        self.difficulty = difficulty
        if difficulty == "Easy":
            self.initial_board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
            self.current_board =  [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]      
        elif difficulty == "Medium":
            self.initial_board = [
            [0, 0, 5, 0, 0, 4, 0, 0, 8],
            [0, 3, 6, 0, 2, 8, 0, 0, 7],
            [0, 8, 4, 0, 1, 0, 0, 6, 0],
            [4, 0, 1, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 5, 0, 1],
            [0, 4, 0, 0, 3, 0, 9, 5, 0],
            [3, 0, 0, 8, 5, 0, 1, 2, 0],
            [1, 0, 0, 6, 0, 0, 7, 0, 0]
        ]
            self.current_board = [
            [0, 0, 5, 0, 0, 4, 0, 0, 8],
            [0, 3, 6, 0, 2, 8, 0, 0, 7],
            [0, 8, 4, 0, 1, 0, 0, 6, 0],
            [4, 0, 1, 0, 0, 0, 0, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 5, 0, 1],
            [0, 4, 0, 0, 3, 0, 9, 5, 0],
            [3, 0, 0, 8, 5, 0, 1, 2, 0],
            [1, 0, 0, 6, 0, 0, 7, 0, 0]
        ]
        elif difficulty == "Hard":
            self.initial_board = [
            [5, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 3, 7, 0, 9, 2, 5, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 3, 0, 6, 0, 0, 0],
            [4, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 5, 0, 0, 0, 1, 8],
            [0, 0, 3, 0, 6, 8, 0, 0, 5],
            [7, 0, 5, 0, 0, 0, 0, 9, 2]
        ]
            
            self.current_board = [
            [5, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 3, 7, 0, 9, 2, 5, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 3, 0, 6, 0, 0, 0],
            [4, 0, 0, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 5, 0, 0, 0, 1, 8],
            [0, 0, 3, 0, 6, 8, 0, 0, 5],
            [7, 0, 5, 0, 0, 0, 0, 9, 2]
        ]
            
    
    
    def find_empty(self):
        """
        Finds the next empty cell in current_board
        :return: (int, int) row, col of empty space
        """
        for i in range(0, 9):
            for j in range(0, 9):
                if self.current_board[i][j] == 0:
                    return (i, j)
        return None
    
    def valid(self, row, col, num):
        """
        Checks if a number is a valid move in the given cell
        :param row: cell row 
               col: cell column
               num: number to be checked
        :return: boolean: whether the number is valid or not
        """
        # Checks column
        for i in range(0, 9):
            if self.current_board[row][i] == num and col != i:
                return False
            
        # Checks row
        for i in range(0, 9):
            if self.current_board[i][col] == num and row != i:
                return False
        
        # Checks the 3x3 box
        box_x = col // 3
        box_y = row // 3
        
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.current_board[i][j] == num and (i, j) != (row, col):
                    return False
                
        return True
    
    def check_victory(self):
        """
        Checks if the current board state is complete (won)
        :return: boolean: whether the current board state reflects a completed
                          board
        """
        for row in range(0, 9):
            for column in range(0, 9):
                if not self.valid(row, column, self.current_board[row][column]):
                    return False
        return True
    
    
    def solve_puzzle(self):
        """
        Solves the sudoku puzzle by updating the current board to reflect
        the completed board using backtracking
        """
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        
        for i in range(1, 10):
            if self.valid(row, col, i):
                self.current_board[row][col] = i
                
                if self.solve_puzzle():
                    return True

                self.current_board[row][col] = 0

        return False
    