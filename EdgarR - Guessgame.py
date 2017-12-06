import random

guesses = 5

print("Hello to Guessgame")
num = input("Guess the number. It is from 1-50. ")

n = random.randint(1, 50)

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1

if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1

if num == (str(n)):
    print(n)
    print("You got it ")

print("You got %d guesses left" % guesses)

num = input("Guess the number. It is from 1-50. ")

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1

if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1

if num == (str(n)):
    print(n)
    print("You got it ")

print("You got %d guesses left" % guesses)

num = input("Guess the number. It is from 1-50. ")

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1

if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1

if num == (str(n)):
    print(n)
    print("You got it ")

print("You got %d guesses left" % guesses)

num = input("Guess the number. It is from 1-50. ")

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1

if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1

if num == (str(n)):
    print(n)
    print("You got it ")

print("You got %d guesses left" % guesses)

num = input("Guess the number. It is from 1-50. ")

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1

if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1

if num == (str(n)):
    print("The number was %s" % n)
    print("You got it ")

if guesses == 0:
    print("You are out of guesses.")

print(n)

print("You got %d guesses left" % guesses)

while guesses > 0 and num != str(n):
    # what I need