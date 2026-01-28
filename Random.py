import random
low=1
high=100
options=["rock","paper","scissors"]
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#number=random.randint(low,high)
number=random.random()
options=random.choice(options)
card=random.choice(cards)
random.shuffle(cards)
print(card)
print(number)
print(options)

