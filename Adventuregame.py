name=input("Enter your name: ")
print("welcome to the adventure game, " + name + "!")
answer=input("You are at a crossroad, do you want to go left or right? ")
if answer=="left":
    answer=input("You come to a river, do you want to swim across or wait for a boat? ")
    if answer=="wait":
        answer=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        if answer=="yellow":
            print("You found the treasure! You Win!")
        elif answer=="red":
            print("It's a room full of fire. Game Over.")
        elif answer=="blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")