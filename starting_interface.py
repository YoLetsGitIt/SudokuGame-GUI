# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 20:31:38 2019

@author: mink9
"""
from tkinter import *

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

        


class Starting_Interface():
    """
    Represents the opening interface to start the game
    
    ...
    
    Buttons
    -------
    popupMenu: 
        A dropdown menu to select the difficulty of the game
    confirm:
        A button to load the game with the currently selected difficulty
    """
    def __init__(self):
        root = Tk()
        root.title("Sudoku")
        
        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, sticky = (N,E,S,W))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe.pack(pady = 100, padx = 200)
        
        difficulty = StringVar(root)
        choices = ["Easy", "Medium", "Hard"]
        difficulty.set("Easy")
        
        popupMenu = OptionMenu(mainframe, difficulty, *choices)
        Label(mainframe, text = "Choose a difficulty").grid(row = 1, column = 1, columnspan = 2)
        popupMenu.grid(row = 2, column = 1)
        confirm = Button(mainframe, text="Confirm", command = lambda: Sudoku_GUI(difficulty.get()))
        confirm.grid(row=2, column=2)
        
        root.mainloop()
        
SudokuGame = Starting_Interface()