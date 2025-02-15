import random
import sys


def guess_game(anwser, guess=None, guesses=0):
    while guess != number:
        guess = int(input(f"Guess a number between {a} and {b}: "))
        guesses += 1
    else:
        if guesses > 1:
            print(f"Congratulations! You guessed in {guesses} tries")
        else:
            print(f"Congratulations! You guessed in {guesses} try")


a = int(sys.argv[1])
b = int(sys.argv[2])

number = random.randint(a, b)

guess_game(number)
