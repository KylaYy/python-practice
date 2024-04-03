import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): \n")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Player choice: {player}\nComputer choice: {computer}")
    if player == computer:
        return "Tied" 
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors"):
        return "Computer win..."
    else:
        return "Player win!"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)