import random

def get_user_choice():
    user_input = input("Enter Rock, Paper, or Scissors: ")
    return user_input.lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "kys mf choose smth else smh"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You won nigga!"
    else:
        return "You lost nigga, womp womp kys!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"I chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Start the game
play_game()