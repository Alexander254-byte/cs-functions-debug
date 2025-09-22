# CS Functions: Modular Code
import random

def get_computer_choice():
    """Computer picks randomly"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    """Decide who wins based on rules"""
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Main game loop"""
    print("=== Rock Paper Scissors ===")
    player_choice = input("Choose rock/paper/scissors: ").lower()
    
    # Input validation (basic debug)
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid! Default to rock.")
        player_choice = "rock"
    
    computer_choice = get_computer_choice()
    print(f"You: {player_choice} | Computer: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Run the function
play_game()