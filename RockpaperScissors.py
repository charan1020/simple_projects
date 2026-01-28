
import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors"):
        print("You win!")
    elif (player == "paper" and computer == "rock"):
        print("You win!")
    elif (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        running = False