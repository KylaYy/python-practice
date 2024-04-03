import random
import time

#variables
playing = True
print("Welcome to Rock, Paper, Scissors! LET'S BEGIN\n")

game_num = 1
game_divider = "~~~~~~~~~~~~~~~~~~"

playing_response = {"y": True, "n": False}

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
    elif player == "rock":
        if computer == "paper":
            return "In a shocking turn of events... Paper wraps Rock! You...... LOSE!!!!!!"
        else:
            return "Impeccable moves.. I'm moved to tears. Rock smashes paper, and YOU WIN!"
    elif player == "paper":
        if computer == "rock":
            return "Marvelous!!!!! With technique like the best gift wrapper, paper wraps rock. You WIN!"
        else:
            return "Snip snip, loser, YOU JUST GOT SHRREEEEDDDDDDDEDDDD!!!!!!!"
    else:
        if computer == "paper":
            return "scissors beat paper! you win!"
        else:
            return "womp womp :( rock beats scissors, you LOSE!!!!! L+RATIO"

#Game loop
while playing:
    time.sleep(0.5)
    print(f"{game_divider} GAME {game_num} {game_divider}")
    
    #gameplay
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    time.sleep(1.5)
    print(result)

    time.sleep(1.5)
    playing = playing_response[input("Would you like to continue? (y or n):\n")]
    game_num+=1

