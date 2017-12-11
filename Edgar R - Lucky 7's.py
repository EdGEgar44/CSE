import random

rounds = 0

money = 15

while money > 0:
    print("Type yes to continues. Type no to stop")
    bet = input("Bet $1 to get four more dollars? ")

    if bet == "yes":
        r = random.randint(1, 6)

        r2 = random.randint(1, 6)

        print("You made a bet of one dollar")

        if (r + r2) == 7:
            money += 5
            print("You won your bet.")
            print("you gain your money and a bonus")
            print("You know have $ %s " % money)
            rounds += 1

        if (r + r2) != 7:
            money -= 1
            print("You lost your bet")
            print("You have  $ %s left." % money)
            rounds += 1

print("You lost all of your money")

print("You did %s rounds." % rounds)
