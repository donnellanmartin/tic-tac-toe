import tkinter as tk
from tkinter import messagebox
import pygame

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Initialize Pygame for playing music
pygame.mixer.init()

# Load and play background music
def play_music():
    pygame.mixer.music.load("")# Insert filepath to your own preffered music 
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Check for winner
def check_winner(player):
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            highlight_winning_line([(row, col) for col in range(3)])
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            highlight_winning_line([(row, col) for row in range(3)])
            return True
    if all([board[i][i] == player for i in range(3)]):
        highlight_winning_line([(i, i) for i in range(3)])
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        highlight_winning_line([(i, 2 - i) for i in range(3)])
        return True
    return False

# Check for a tie
def check_tie():
    return all([spot != " " for row in board for spot in row])

# Highlight winning line
def highlight_winning_line(winning_coords):
    for row, col in winning_coords:
        buttons[row][col].config(bg="yellow")

# Handle button clicks and player turns
def on_click(row, col):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        color = "red" if current_player == "X" else "green"
        buttons[row][col].config(text=current_player, state="disabled", fg=color, font=("Helvetica", 48, "bold"))
        buttons[row][col].update_idletasks()
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game board
def reset_game():
    global current_player, board
    current_player = "X"
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal", font=("Helvetica", 48, "bold"), fg="black", bg="SystemButtonFace")

# Quit the game
def quit_game():
    pygame.mixer.music.stop()
    root.quit()

# Create the grid buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=" ", width=10, height=3, command=lambda row=row, col=col: on_click(row, col),
                           font=("Helvetica", 48, "bold"), fg="black", bg="SystemButtonFace")
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Add a quit button
quit_button = tk.Button(root, text="Quit", command=quit_game, font=("Helvetica", 16), bg="lightgray")
quit_button.grid(row=3, column=1, pady=10)

# Start the music
play_music()

# Start the GUI
root.mainloop()
