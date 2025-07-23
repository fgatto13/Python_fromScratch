# Python quitz game
import time

questions = ("How many elements are in the periodic table?: ", 
            "Which animal lays the largest eggs?: ", 
            "What is the most abundant gas in Earth's atmosphere?: ", 
            "How many bones are in the human body?: ", 
            "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = [] # we will be appending guesses to the list, hence the reason why we're not using tuples for that
score = 0
question_num = 0 # keeps track of the current question number

for question in questions:
    time.sleep(.5)
    print("---------------")
    print(question)
    time.sleep(1)
    for option in options[question_num]:
        time.sleep(1)
        print(option)
    print()
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    time.sleep(.5)
    if guess == answers[question_num]:
        score += 1
        print("Correct! ")
    else:
        print("Incorrect!")
        print(f"The answer for question {question_num} is {answers[question_num]}")
    time.sleep(.5)
    question_num += 1

print("---------------")
print("    RESULTS    ")
print("---------------")

time.sleep(1)

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

time.sleep(1)

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

time.sleep(1)

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")