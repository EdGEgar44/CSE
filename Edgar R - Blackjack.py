import random

card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "A", "J", "K", "Q"]

player_One_BlackJack = "False"

dealer_BlackJack = "False"

print("Welcome to BlackJack.")

while player_One_BlackJack != "True" or dealer_BlackJack != "True":

    dealer_card1 = card_list[random.randint()]

    dealer_card2 = random.randint(2, 12)

    player_one_card1 = random.randint(2, 12)

    player_one_card2 = random.randint(2, 12)

    if dealer_card1 == "J" or "K" or "Q":
        dealer_card1 = 10

    if dealer_card2 == "J" or "K" or "Q":
        dealer_card2 = 10

    if player_one_card1 == "J" or "K" or "Q":
        dealer_card1 = 10

    if player_one_card2 == "J" or "K" or "Q":
        player_one_card2 = 10

    print("Your card %s" % player_one_card1)

    print("Your card %s" % player_one_card2)

    dealer_added = dealer_card1 + dealer_card2

    player_one_added = player_one_card1 + player_one_card2

    print("Together, the card are equal to %s." % player_one_added)

    print("Dealer right_side up is %s" % dealer_card2)

    if dealer_added > 21:
        if dealer_card2 == "A" and dealer_card1 == "A":
            dealer_card1 = 1
        if dealer_card1 == "A":
            dealer_card1 = 1

    if player_one_added or dealer_added < 21:
        new_card = input("Would you like to get another card?(Yes or No) ")

        if new_card == "Yes":
            player_one_card3 = random.randint(2, 12)

            if dealer_added > 21:
                dealer_card3 = random.randint(2, 12)

            if dealer_card3 == 12:
                dealer_card3 = "A"

            if player_one_card3 == 12:
                player_one_card3 = "A"

            player_one_added = player_one_added + player_one_card3

            dealer_added = dealer_added + dealer_card3

            print("Your new card is %s" % player_one_card3)

            print("Together, the cards are equal to %s." % player_one_added)

            if player_one_added or dealer_added < 21:
                new_card2 = input("Would you like get another card?(Yes or No) ")

                if new_card2 == "Yes":
                    player_one_card4 = random.randint(2, 12)

                if new_card2 == "No":
                    print("You are not going to get a new card.")

        if new_card == "No":
            print("You are not going to get any more cards.")

    if player_one_added or dealer_added > 21:
        if player_one_added > 21:
            print("You Busted. The dealer Won.")
            print("The dealers card were %s." % player_one_added)

        if dealer_added > 21:
            print("You won. The dealer lost.")