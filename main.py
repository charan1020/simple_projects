#if__name__=="__main__":(this scriptcan be imported or run standalone)
#functions and in this module can be reused without the main block of code executing
from main1 import favorite_food


def favorite_drink(drink):
    print(f"My favorite drink is {drink}")
def main():
    print("This is the main function.")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye!")
if __name__ == "__main__":
    main()
