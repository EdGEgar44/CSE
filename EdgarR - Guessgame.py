import random

guess = 5

print("Hello to Guessgame")
num = input("Guess the number. It is from 1-50. ")

n = input(random.randint(1, 50))

if guess <= n:
    # print("Higher")
    guess -= 1

if guess >= n:
    # print("Lower")
    guess -= 1
    print("Try again")
