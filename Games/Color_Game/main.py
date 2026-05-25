import random
import tkinter as tk
from tkinter import messagebox

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
score = 0
timeleft = 30

def next_colour():
    global score, timeleft

    if timeleft > 0:
        user_input = e.get().lower()

        # Get actual text color (correct answer)
        correct_color = label.cget("fg").lower()

        if user_input == correct_color:
            score += 1

        e.delete(0, tk.END)
        random.shuffle(colours)

        # Display word and different color
        label.config(fg=colours[0], text=colours[1])

        score_label.config(text=f"Score: {score}")


def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        time_label.config(text=f"Time left: {timeleft}")
        window.after(1000, countdown)
    else:
        scoreshow()


def record_highest_score():
    highest_score = load_highest_score()

    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))


def load_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            data = file.read()
            return int(data) if data else 0
    except FileNotFoundError:
        return 0


def scoreshow():
    record_highest_score()

    # Use Toplevel instead of Tk()
    window2 = tk.Toplevel(window)
    window2.title("HIGH SCORE")
    window2.geometry("300x200")

    label2 = tk.Label(window2,
                      text=f"Highest Score: {load_highest_score()}",
                      font=(font, 12))
    label2.pack(pady=20)


def start_game(event):
    global timeleft

    if timeleft == 30:
        countdown()

    next_colour()


# ---------------- MAIN WINDOW ---------------- #

window = tk.Tk()
font = 'Helvetica'

window.title("Color Game")

# ✅ FIXED ICON ERROR (safe handling)
try:
    window.iconbitmap(r"D:\My Program\Python Projects\Color_Game\color_game_icon.ico")
except:
    print("Icon not found, skipping...")

window.geometry("375x250")
window.resizable(False, False)

instructions = tk.Label(window,
                        text="Enter the color of the text, not the word!",
                        font=(font, 12))
instructions.pack(pady=10)

score_label = tk.Label(window,
                       text="Press Enter to start",
                       font=(font, 12))
score_label.pack()

time_label = tk.Label(window,
                      text=f"Time left: {timeleft}",
                      font=(font, 12))
time_label.pack()

label = tk.Label(window, font=(font, 60))
label.pack(pady=20)

e = tk.Entry(window)
e.pack()
e.focus_set()

window.bind('<Return>', start_game)

window.mainloop()