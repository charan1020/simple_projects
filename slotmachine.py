import random
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    results=[random.choice(symbols) for _ in range(3)]
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
def print_row(row):
    print("*************************")
    print(" | ".join(row))
    print("*************************")
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*10
        elif row[0]=='🍉':
            return bet*20
        elif row[0]=='🍋':
            return bet*30
        elif row[0]=='🔔':
            return bet*40
        elif row[0]=='⭐':
            return bet*50
    return 0
def main():
    balance=100
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("*************************")
    while balance>0:
        print(f"Current Balance: ${balance}")
        bet=(input("Enter your bet amount (or 0 to quit): "))
        if not bet.isdigit():
            print("Invalid input. Please enter a numeric value.")
            continue
        bet=int(bet)
        if bet>balance:
            print("Bet exceeds current balance. Please enter a valid bet.")
            continue
        if bet<=0:
            print("Bet must be greater than zero to play. Exiting game.")
            continue
        balance-=bet
        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, no win this time.")
        balance+=payout
        play_again=input("Do you want to play again? (y/n): ").lower()
    print("Game over! You have run out of balance. Thank you for playing!")

if __name__=="__main__":
    main()
