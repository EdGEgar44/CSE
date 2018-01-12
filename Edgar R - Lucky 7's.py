import random

stop_at_round = 0

rounds = 0

money = 15

most_money = 15

left_over_money = 0

while money > 0:

    r = random.randint(1, 6)

    r2 = random.randint(1, 6)

    print("You made a bet of one dollar")

    if (r + r2) == 7:
        money += 4
        print("You won your bet.")
        print("you gain your money and a bonus")
        print("You know have $%s left. " % money)
        rounds += 1

    if money >= most_money:
        left_over_money = (money - most_money)
        most_money = left_over_money + most_money
        stop_at_round = rounds

    if (r + r2) != 7:
        money -= 1
        print("You lost your bet")
        print("You have $%s left." % money)
        rounds += 1

print("You lost all of your money")

print("You did %s rounds." % rounds)

if stop_at_round == 0:
    print("The most money you had was $%s." % most_money)
    print("You shouldn't even have played this game.")
else:
    print("The most money you had was $%s." % most_money)
    print("You should have stopped at round %s." % stop_at_round)
