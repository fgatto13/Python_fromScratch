# Number guessing game in Python using the random library
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome! Python Number Guessing Name")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Number out of range")
            print(f"Please, Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! try again!")
        elif guess > answer:
            print("Too high! try again!")
        else:
            print("You guessed right! Well done!")
            print(f"You took {guesses} times to get it right")
            is_running = False
                
    else:
        print("invalid guess")
        print(f"Please, Select a number between {lowest_num} and {highest_num}")