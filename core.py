import tkinter as tk
import random

# Initialize scores
user_score = 0
ai_score = 0

# Function to determine the winner and update the scoreboard
def determine_winner(user_choice):
    global user_score, ai_score
    choices = ['Rock', 'Paper', 'Scissors']
    ai_choice = random.choice(choices)
   
    if user_choice == ai_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and ai_choice == 'Scissors') or \
         (user_choice == 'Paper' and ai_choice == 'Rock') or \
         (user_choice == 'Scissors' and ai_choice == 'Paper'):
        result = "You win!"
        user_score += 1
    else:
        result = "AI wins!"
        ai_score += 1

    # Update labels with choices, result, and scoreboard
    user_choice_label.config(text=f"Your choice: {user_choice}")
    ai_choice_label.config(text=f"AI's choice: {ai_choice}")
    result_label.config(text=result)
    user_score_label.config(text=f"Your Score: {user_score}")
    ai_score_label.config(text=f"AI Score: {ai_score}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x450")
root.configure(bg="#33334d")

# Title label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#33334d", fg="#f2f2f2")
title_label.pack(pady=10)

# Labels to show choices, result, and scoreboard
user_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 12), bg="#33334d", fg="#b3b3cc")
user_choice_label.pack()

ai_choice_label = tk.Label(root, text="AI's choice: ", font=("Arial", 12), bg="#33334d", fg="#b3b3cc")
ai_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#33334d", fg="#ff6666")
result_label.pack(pady=10)

# Scoreboard
score_frame = tk.Frame(root, bg="#33334d")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12), bg="#33334d", fg="#80ff80")
user_score_label.grid(row=0, column=0, padx=10)

ai_score_label = tk.Label(score_frame, text="AI Score: 0", font=("Arial", 12), bg="#33334d", fg="#ff8080")
ai_score_label.grid(row=0, column=1, padx=10)

# Button frame to center the buttons
button_frame = tk.Frame(root, bg="#33334d")
button_frame.pack(pady=20)

# Button styling
button_style = {
    "font": ("Arial", 12, "bold"),
    "bg": "#4d4dff",
    "fg": "#f2f2f2",
    "width": 10,
    "height": 2,
    "relief": tk.RAISED,
}

# Buttons for user choices
rock_button = tk.Button(button_frame, text="Rock", command=lambda: determine_winner("Rock"), **button_style)
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: determine_winner("Paper"), **button_style)
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: determine_winner("Scissors"), **button_style)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Powered by OpenAI platinum box at the bottom
footer_frame = tk.Frame(root, bg="#e5e4e2", width=400, height=30)
footer_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its content
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(footer_frame, text="Вдъхновение за бизнес и жажда за знания!", font=("Arial", 10, "italic"), bg="#e5e4e2", fg="#33334d")
footer_label.pack()

# Runs the application
root.mainloop()
