import tkinter as tk
from tkinter import messagebox


def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return [(i, j) for j in range(3)]
        if all([board[j][i] == player for j in range(3)]):
            return [(j, i) for j in range(3)]
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return [(0, 2), (1, 1), (2, 0)]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def on_button_click(row, col, buttons, board, current_player_var):
    current_player = current_player_var.get()  
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled", disabledforeground="black", bg="#FFD700")

        winner_positions = check_winner(board, current_player)
        if winner_positions:
            for r, c in winner_positions:
                buttons[r][c].config(bg="green")
            messagebox.showinfo("Перемога!", f"Гравець {current_player} виграв!")
            reset_game(board, buttons, current_player_var)
        elif is_board_full(board):
            messagebox.showinfo("Нічия", "Нічия!")
            reset_game(board, buttons, current_player_var)
        else:
            next_player = "O" if current_player == "X" else "X"
            current_player_var.set(next_player)

def reset_game(board, buttons, current_player_var):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text=" ", state="normal", bg="#333", fg="black")
    current_player_var.set("X")

root = tk.Tk()
root.title("Хрестики-Нолики")
root.configure(bg="#222")

current_player_var = tk.StringVar(value="X") 
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3,
                                  font=("Arial", 20, "bold"), bg="#333", fg="black", activebackground="#FFD700",
                                  command=lambda row=i, col=j: on_button_click(row, col, buttons, board, current_player_var))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_button = tk.Button(root, text="Скинути гру", width=20, height=2, font=("Arial", 14), bg="#555", fg="white",
                          activebackground="#FF4500", command=lambda: reset_game(board, buttons, current_player_var))
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
