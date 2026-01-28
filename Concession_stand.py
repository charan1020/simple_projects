menu={"popcorn": 5.00, "pizza": 10.00, "fries": 3.00, "drink": 2.00,"chicken nuggets": 6.00 }
cart=[]
total=0
print("Welcome to the Concession Stand!")
print("Here is the menu:")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
while True:
    food =input("select an item(q to quit):")
    if food.lower()=="q":
        break
    elif menu.get(food.lower()) is not None:
        cart.append(food.lower())
for food in cart:
        total+=menu[food.lower()]
        print(food,end=" ")
print()
print(f"Total is: ${total:.2f}")
