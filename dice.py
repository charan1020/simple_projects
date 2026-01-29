import random
print("\u25CF \u25CF \u25CF \u25CF \u25CF \u25CF \u25CF")
dice_art={
    1:("\u25CF     \n"),
    2:("\u25CF \u25CF \n"),
    3:("\u25CF \u25CF \u25CF \n"),
    4:("\u25CF \u25CF \n\u25CF \u25CF \n"),
    5:("\u25CF \u25CF \n\u25CF     \n\u25CF \u25CF \n"),
    6:("\u25CF \u25CF \n\u25CF \u25CF \n\u25CF \u25CF\n")
}
dice=[]
total=0
num_of_dice=int(input("How many dice would you like to roll? "))
for _ in range(num_of_dice):
    roll=random.randint(1,6)
    dice.append(roll)
    total+=roll