import random

player_One_BlackJack = "False"

dealer_BlackJack = "False"

while player_One_BlackJack != "True" or dealer_BlackJack != "True":

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

    print("Your card %s" % player_one_card1)

    print("Your card %s" % player_one_card2)

    dealer_added = dealer_card1 + dealer_card2

    player_one_added = player_one_card1 + player_one_card2

    print("Together, the card are equal to %s." % player_one_added)

    print("Dealer right_side up is %s" % dealer_card2)

    if player_one_added < 21:
        new_card = input("Would you like to get another card?(Yes or No) ")

        print(dealer_card1)

        if new_card == "Yes":
            player_one_card3 = random.randint(2, 12)

            if player_one_card3 == 12:
                player_one_card3 = "A"

            player_one_added = player_one_added + player_one_card3

            print("Your new card is %s" % player_one_card3)

            print("Together, the cards are equal to %s." % player_one_added)

        if new_card == "No":
            print("nothing")

    if player_one_added > 21 or dealer_added > 21:
        if player_one_added > 21:
            print("You Busted. The dealer Won.")
            print("The dealers card were %s." % player_one_added)

        if dealer_added > 21:
            print("You won. The dealer lost.")
