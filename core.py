import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    ai_choice = random.choice(choices)
    
    result = ""
    if user_choice == ai_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and ai_choice == 'Scissors') or \
         (user_choice == 'Paper' and ai_choice == 'Rock') or \
         (user_choice == 'Scissors' and ai_choice == 'Paper'):
        result = "You win!"
    else:
        result = "AI wins!"

    # Update labels with results
    user_choice_label.config(text=f"Your choice: {user_choice}")
    ai_choice_label.config(text=f"AI's choice: {ai_choice}")
    result_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x200")

# Labels to show choices and result
user_choice_label = tk.Label(root, text="Your choice: ")
user_choice_label.pack()

ai_choice_label = tk.Label(root, text="AI's choice: ")
ai_choice_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
rock_button.pack(side=tk.LEFT, padx=10, pady=20)

paper_button = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
paper_button.pack(side=tk.LEFT, padx=10, pady=20)

scissors_button = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10, pady=20)

# Run the application
root.mainloop()
