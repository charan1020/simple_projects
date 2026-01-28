import random
lowest_number=1
highest_number=100
answer=random.randint(lowest_number,highest_number)
guess=0
is_running=True
print("Welcome to the Guessing Game!")
print(f"I'm thinking of a number between {lowest_number} and {highest_number}. Can you guess it?")
while is_running:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess < lowest_number or guess > highest_number:
        print(f"Please guess a number within the range of {lowest_number} to {highest_number}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the correct number: {answer}")
        is_running = False