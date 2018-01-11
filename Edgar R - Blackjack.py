import random

player_One_BlackJack = "False"

dealer_BlackJack = "False"

while player_One_BlackJack != "False" or dealer_BlackJack != "False":

    dealer_card1 = random.randint(2, 12)

    dealer_card2 = random.randint(2, 12)

    player_one_card1 = random.randint(2, 12)

    player_one_card2 = random.randint(2, 12)

    if dealer_card2 == 12:
        dealer_card2 = "A"

    if dealer_card1 == 12:
        dealer_card1 = "A"

    if player_one_card1 == 12:
        dealer_card1 = "A"

    if player_one_card2 == 12:
        player_one_card2 = "A"

    print(player_one_card1)

    print(player_one_card2)
