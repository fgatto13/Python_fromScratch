import time

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")
    time.sleep(1)

def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("You cannot deposit negative amount")
        time.sleep(1)
        return 0
    else:
        print(f"Your deposit is: ${amount}")
        time.sleep(1)
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount < 0:
        print("You cannot withdraw negative amount")
        time.sleep(1)
        return 0
    elif amount > balance:
        print("You don't have enough money")
        time.sleep(1)
        return 0
    else:
        print(f"Your withdraw is: ${amount}")
        time.sleep(1)
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print("********************")
        print("banking program")
        print("********************")

        print("1. show balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. exit")

        print("********************")
        choice = int(input("Enter your choice (1, 2, 3, 4): "))
        print("********************")
        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("Invalid choice")
    print("Thank you for using banking program")

if __name__ == "__main__":
    main()