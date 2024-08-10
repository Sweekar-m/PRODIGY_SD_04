import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry('600x550')
        self.root.resizable(False, False)
        self.root.configure(bg='#f7f7f7')

        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(root, width=3, font=('Arial', 18), justify='center',
                                 highlightthickness=1, highlightbackground='#a9a9a9', bg='#eaeaea')
                entry.grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=5)
                row.append(entry)
            self.entries.append(row)

        solve_button = tk.Button(root, text="Solve", command=self.solve,
                                 font=('Arial', 14), bg='#4caf50', fg='white', activebackground='#45a049')
        solve_button.grid(row=9, column=0, columnspan=4, pady=10, ipadx=10, ipady=5)

        clear_button = tk.Button(root, text="Clear", command=self.clear_grid,
                                 font=('Arial', 14), bg='#f44336', fg='white', activebackground='#e53935')
        clear_button.grid(row=9, column=5, columnspan=4, pady=10, ipadx=10, ipady=5)

    def get_board(self):
        board = []
        for row in self.entries:
            board_row = []
            for entry in row:
                value = entry.get()
                if value == '':
                    board_row.append(0)
                else:
                    board_row.append(int(value))
            board.append(board_row)
        return board

    def set_board(self, board):
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                self.entries[i][j].delete(0, tk.END)
                if num != 0:
                    self.entries[i][j].insert(0, str(num))

    def clear_grid(self):
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

    def is_valid(self, board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve_board(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve(self):
        board = self.get_board()
        if self.solve_board(board):
            self.set_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for the provided Sudoku.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
