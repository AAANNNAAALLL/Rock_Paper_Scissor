import tkinter as tk
import random
import pygame

# Initialize pygame for sounds
pygame.init()
pygame.mixer.init()

# Load a start sound (optional, replace with your own file)
try:
    start_sound = pygame.mixer.Sound("start.wav")
except:
    start_sound = None

choices = ["Rock", "Paper", "Scissors"]
icons = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

# Game Logic with Hand Shake Animation
def play(user_choice, game_root, user_label, comp_label, result_label):
    computer_choice = random.choice(choices)

    frames = 6  # number of shakes
    current = 0
    hands = ["✊", "✋", "✌️"]  # cycle during shaking

    def shake():
        nonlocal current
        if current < frames:
            user_label.config(text=random.choice(hands), font=("Arial", 40))
            comp_label.config(text=random.choice(hands), font=("Arial", 40))
            current += 1
            game_root.after(300, shake)  # speed of shaking
        else:
            # Show final choices
            user_label.config(text=icons[user_choice], font=("Arial", 40))
            comp_label.config(text=icons[computer_choice], font=("Arial", 40))

            # Decide winner
            if user_choice == computer_choice:
                result = "It's a Tie!"
            elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                 (user_choice == "Paper" and computer_choice == "Rock") or \
                 (user_choice == "Scissors" and computer_choice == "Paper"):
                result = "You Win!"
            else:
                result = "You Lose!"

            result_label.config(text=result, font=("Arial", 16, "bold"), fg="blue")

    shake()

# Start Game Function
def start_game():
    if start_sound:
        start_sound.play()
    game_window()

# Tkinter GUI for the game
def game_window():
    game_root = tk.Tk()
    game_root.title("Rock Paper Scissors Game 🎮")
    game_root.geometry("500x500")

    tk.Label(game_root, text="Rock ✊ Paper ✋ Scissors ✌️", font=("Arial", 14)).pack(pady=10)

    frame = tk.Frame(game_root)
    frame.pack(pady=20)

    user_label = tk.Label(frame, text="❔", font=("Arial", 40))
    user_label.grid(row=0, column=0, padx=40)

    vs_label = tk.Label(frame, text="VS", font=("Arial", 20))
    vs_label.grid(row=0, column=1)

    comp_label = tk.Label(frame, text="❔", font=("Arial", 40))
    comp_label.grid(row=0, column=2, padx=40)

    result_label = tk.Label(game_root, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    # Buttons
    tk.Button(game_root, text="Rock ✊", width=15, height=2,
              command=lambda: play("Rock", game_root, user_label, comp_label, result_label)).pack(pady=5)
    tk.Button(game_root, text="Paper ✋", width=15, height=2,
              command=lambda: play("Paper", game_root, user_label, comp_label, result_label)).pack(pady=5)
    tk.Button(game_root, text="Scissors ✌️", width=15, height=2,
              command=lambda: play("Scissors", game_root, user_label, comp_label, result_label)).pack(pady=5)

    game_root.mainloop()

menu = tk.Tk()
menu.title("Launch Menu")
menu.geometry("300x200")

tk.Label(menu, text="Welcome to Rock Paper Scissors 🎮", font=("Arial", 12)).pack(pady=20)
tk.Button(menu, text="Start Game", width=20, height=2, command=start_game).pack(pady=20)
tk.Button(menu, text="Exit", width=20, height=2, command=menu.destroy).pack()

menu.mainloop()
