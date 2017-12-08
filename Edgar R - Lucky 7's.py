import random

rounds = 0

money = 15

r = random.randint(1, 6)
r2 = random.randint(1, 6)



while money > 0:
    if (r + r2) == 7:
        print("you gain ")