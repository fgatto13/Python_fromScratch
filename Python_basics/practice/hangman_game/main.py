# import random
# from wordslist import words
from getpass import getpass
# variables

# dictionary of key:() (tuple)
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

# functions

# the display_man function takes as a parameter the number of wrong guesses
# so that we can display the correspondent man

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint): # we pass a list of hints
    print(" ".join(hint))
def display_guesses(guessed_letters):
    print("Guessed letters: ", ", ".join(guessed_letters))

def display_answer(answer):
    print(" ".join(answer))

def main():
    play_again = True
    # answer = random.choice(words)
    while play_again:
        answer = getpass("Insert the word: ")
        hint = ["_"] * len(answer) # we want the number of _ to be the length of the answer

        # note: when using lists, multiplying it by a certain value,
        # duplicates the elements of the list for set number of times

        wrong_guesses = 0
        guessed_letters = set()
        is_running = True

        while is_running:

            display_guesses(guessed_letters)
            display_man(wrong_guesses)
            display_hint(hint)

            guess = input("Guess a letter: ").lower()

            # input validation:
            # we both check if it is not a single digit and if it has a number
            if len(guess) != 1 or not guess.isalpha():
                print("Sorry, that's not a single letter.")
                # if it's not valid, we skip this iteration
                continue

            # now we want to check whether the letter has already been guessed
            if guess in guessed_letters:
                print("Sorry, that letter was already guessed.")
                # if so, we skip this iteration
                continue
            # then, we can add the guessed letter to the set of guesses
            guessed_letters.add(guess)

            # we now want to check if the letter is in the answer
            if guess in answer:
                # if that's the case, we want to iterate the answer
                for i in range(len(answer)):
                    # everytime the letter at index i is equal to the guess
                    if answer[i] == guess:
                        # we substitute _ with the guessed letter
                        hint[i] = guess
            else:
                # otherwise, we increment the number of wrong guesses
                wrong_guesses += 1

            # win condition
            if "_" not in hint:
                display_man(wrong_guesses)
                display_answer(answer)
                print("Congratulations, you guessed the word!")
                is_running = False
            # lose condition
            elif wrong_guesses >= len(hangman_art) - 1:
                display_man(wrong_guesses)
                display_answer(answer)
                print("Sorry, you lost.")
                is_running = False
        if input("Wanna play again? (y/n): ").lower() == "n":
            play_again = False

if __name__ == "__main__":
    main()