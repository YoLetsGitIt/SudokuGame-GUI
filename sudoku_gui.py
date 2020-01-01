# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:23:43 2020

@author: mink9
"""

class Sudoku_GUI():
    """
    Class to represent the UI of the game
    
    ...
    
    Attributes
    ----------
    difficulty: str
        The difficulty of the game
    game: Sudoku_Game
        Game object
    GUI: Tk
        Tkinter object, representing the user interface
    row: int
        Row of selected cell
    col: int
        Column of selected cell
    canvas: Canvas
        Canvas on the GUI where all the objects are drawn on
    
    Methods
    -------
    initUI()
        Draws the template of the game
    clear_answers()
        Clears the currently inputed numbers
    solve()
        Solves the current puzzle, leading to victory
    draw_grid()
        Draws the grids of the puzzle
    draw_number(row, col, num)
        Inputs the number in the given row and column (cell)
    draw_numbers(board)
        Draws the numbers in the given board
    cell_clicked(event)
        When left clicked, selects the clicked cell and prompts draw_cursor()
    draw_cursor()
        Draws a red outlining box on the currently selected cell
    key_pressed(event)
        Draws the key pressed (if valid) in the currently selected cell
    print_victory()
        Draws a yellow oval with the word "Victory"
    
    
    """
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.game = Sudoku_Game(difficulty)
        self.GUI = Tk()
        self.GUI.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        self.GUI.title("Sudoku - Difficulty " + difficulty)
    
        self.row, self.col = -1, -1
            
        self.initUI()
        
    def initUI(self):
        """
        Draws the template of the game
        """
        self.canvas = Canvas(self.GUI,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self.GUI,
                              text="Clear answers", command = self.clear_answers)
        clear_button.pack(side=LEFT)
        solve_button = Button(self.GUI, 
                              text = "Solve Puzzle", command = self.solve)
        solve_button.pack(side=RIGHT)
        
        self.draw_grid()
        self.draw_numbers(self.game.initial_board)
        
        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)
    
    def clear_answers(self):
        """
        Deletes all currently inputed answers
        """
        self.game = Sudoku_Game(self.difficulty)
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_numbers(self.game.current_board)
        
    def solve(self):
        """
        Solves the current puzzle, leading to victory
        """
        # Resets current_board back to its initial state in order to run
        # solve_puzzle()
        for i in range(0, 9):
            for j in range(0, 9):
                self.game.current_board[i][j] = self.game.initial_board[i][j]
        self.canvas.delete(ALL)
        self.game.solve_puzzle()
        self.draw_grid()
        self.draw_numbers(self.game.current_board)
        self.print_victory()
        
        
    def draw_grid(self):
        """
        Draws the grids of the puzzle
        """
        for i in range(0, 10):
            color = "blue" if i % 3 == 0 else "gray"
    
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    
            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
                
    def draw_number(self, row, col, num):
        """
        Inputs the number in the given row and column (cell)
        :param row: the row of the cell where the number will be inputed
               col: the column of the cell where the number will be inputed
               num: the number which will be inputed into the cell
        """
        x = MARGIN + col * SIDE + SIDE / 2
        y = MARGIN + row * SIDE + SIDE / 2
        if self.game.initial_board[row][col] == self.game.current_board[row][col]:
            color = "black"
        else:
            color = "sea green"
        self.game.text_tracker[col][row] = self.canvas.create_text(
                x, y, text=num, tags="numbers", fill=color
                )
    
    def draw_numbers(self, board):
        """
        Draws the numbers in the given board
        :param board: the board which will be drawn
        """
        for i in range(0, 9):
            for j in range(0, 9):
                answer = board[i][j]
                if answer != 0:
                    self.draw_number(i, j, answer)
    
    def cell_clicked(self, event):
        """
        When left clicked, selects the clicked cell and prompts draw_cursor()
        :param: event: The left click event prompted by the user
        """
        x, y = event.x, event.y
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE
    
            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.initial_board[row][col] == 0:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1
    
        self.draw_cursor()
    
    def draw_cursor(self):
        """
        Draws a red outlining box on the currently selected cell
        """
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )
        
    def key_pressed(self, event):
        """
        Draws the key pressed (if valid) in the currently selected cell
        :param: event: The event object prompted when the keyboard is pressed
        """
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            self.game.current_board[self.row][self.col] = int(event.char)
            x = MARGIN + self.col * SIDE + SIDE / 2
            y = MARGIN + self.row * SIDE + SIDE / 2
            if (int(event.char) != 0):
                self.canvas.delete(self.game.text_tracker[self.col][self.row])
                if self.game.valid(self.row, self.col, int(event.char)):
                    self.draw_number(self.row, self.col, int(event.char))
                    self.col, self.row = -1, -1
                    self.draw_cursor()
                else:
                    self.draw_number(self.row, self.col, int(event.char))
        if self.game.check_victory():
            self.print_victory()
                    
    def print_victory(self):
        """
        Draws a yellow oval with the word "Victory"
        """
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="dark orange", outline="orange"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32)
        )