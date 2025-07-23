import random

options = ("rock", "paper", "scissors")
running = True

while running:
    
    player = None # player's choice
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choiche (rock, paper, scissors): ").lower()
        if player not in options:
            print("You have to choose between rock, paper and scissors, try again")
            
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == computer:
        print("Tie")
    # check if one of the winning conditions is met
    elif player == "rock" and computer == "scissors":
        print("You Won!")
    elif player == "paper" and computer == "rock":
        print("You Won!")
    elif player == "scissors" and computer == "paper":
        print("You Won!")
    # if none is met, then you lost
    else:
        print("You lost")
        
    if not input("Would you like another go? y to continue, or enter any key to exit: ").lower() == "y":
       running = False
       
print("Thanks for playing!")