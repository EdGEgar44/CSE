import random

guesses = 5

print("Hello to Guessgame")

n = random.randint(1, 50)

num = input("Guess the number. It is from 1-50. ")

if num < (str(n)):
    print("Higher")
    print("Try again")
    guesses -= 1
    print("Guesses: %d " % guesses)


if num > (str(n)):
    print("Lower")
    print("Try again")
    guesses -= 1
    print("guesses left :%d" % guesses)


while guesses > 0 and num != str(n):
    num = input("Guess the number. It is from 1-50. ")
    if num < (str(n)):
        print("Higher")
        print("Try again")
        guesses -= 1
        print("You got %d guesses left" % guesses)

    if num > (str(n)):
        print("Lower")
        print("Try again")
        guesses -= 1
        print("You got %d guesses left" % guesses)

if guesses == 0:
    print("You didn't guesses the correct number")
    print("The number was %d" % n)

if guesses > 0 and num == str(n):
    print("You got it right with %s guesses left" % guesses)
    print("The number was %d" % n)
