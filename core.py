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
root.geometry("300x250")

# Labels to show choices, result, and scoreboard
user_choice_label = tk.Label(root, text="Your choice: ")
user_choice_label.pack()

ai_choice_label = tk.Label(root, text="AI's choice: ")
ai_choice_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Scoreboard
score_frame = tk.Frame(root)
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="Your Score: 0")
user_score_label.grid(row=0, column=0, padx=10)

ai_score_label = tk.Label(score_frame, text="AI Score: 0")
ai_score_label.grid(row=0, column=1, padx=10)

# Button frame to center the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons for user choices
rock_button = tk.Button(button_frame, text="Rock", command=lambda: determine_winner("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: determine_winner("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: determine_winner("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
