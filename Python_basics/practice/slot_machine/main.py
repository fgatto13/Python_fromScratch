import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐️"]
    return [random.choice(symbols) for _ in range(3)] # for every iteration in range(3), return a symbol

def print_row(row):
    print(" ".join(row)) # we use the join function to separate the elements in the row with a space

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍒':
                return bet * 3
            case '🍉':
                return bet * 4
            case '🍋':
                return bet * 5
            case '🔔':
                return bet * 10
            case '⭐':
                return bet * 20
    return 0

def main():
    balance = 100

    print("********************")
    print("Welcome to Slot-Machine!")
    print("Symbols: 🍒🍉🍋🔔⭐️")
    print("********************")

    while balance > 0:
        print(f"Current balance is: ${balance:.2f}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter a number.")
            continue

        bet = int(bet)
        if bet > balance:
            print("Sorry, you don't have enough money.")
            continue
        if bet < 0:
            print("you cannot bet a negative number.")
            continue

        balance -= bet

        row = spin_row() # row is a list
        print("Spinning...")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Your payout is: ${payout:.2f}")
        else:
            print("Sorry, you lost this round.")

        balance += payout

        play_again = input("Would you like to play again? (y/n): ").upper()
        if play_again != 'Y':
            break
    print(f"Thank you for playing. Final balance is: ${balance:.2f}")

if __name__ == "__main__":
    main()