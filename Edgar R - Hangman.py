import random
import string

guesses_left = 10

player_stop_playing = "False"

word_phrase_bank = ["Classwork", "Train", "Computer", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]

guessed_words = []

while player_stop_playing != "True":

    play_a_game = input("Do you want to play a game of Hangman?(Yes or no) ")

    play_a_game = play_a_game.lower()

    word_selector = random.choice(word_phrase_bank)

    word_selector_stars_list = list(word_selector_stars)

    while play_a_game == "yes" and guesses_left >= 0:

        range_of_letter = len(word_selector)

        word_selector_stars = range_of_letter * "*"

        if word_selector == "Mr.Wiebe":
            word_selector_stars = "**.*****"

        word_selector = word_selector.lower()

        word_selector = list(word_selector)

        while guesses_left >= 0:

            if guessed_words == str([]):
                print("These are the words you have guessed %s " % guessed_words)

            print("You have %s guesses left." % guesses_left)

            print(word_selector_stars)

            print(word_selector)

            word_guessed = input("Guess the letter. ")

            word_guessed = word_guessed.lower()

            if word_guessed != word_selector:
                word_guessed = guessed_words.append(word_guessed)
                print("Try again")
                guesses_left -= 1

            print(guessed_words)

            if word_selector == "classwork" and word_guessed == "c" or "l" or "a" or "s" or "w" or "o" or "r" or "k":
                print("You got it right!")
                if word_guessed == "c":
                    word_selector_stars_list[0] = "c"

                if word_guessed == "l":
                    word_selector_stars_list[1] = "l"

                if word_selector_stars == "a":
                    word_selector_stars_list[2] = "a"

                if word_selector_stars == "s":
                    word_selector_stars_list[3, 4] = "s"

                if word_selector_stars == "w":
                    word_selector_stars_list[5] = "w"

                if word_selector_stars == "o":
                    word_selector_stars_list[8] = "o"

                if word_selector_stars == "r":
                    word_selector_stars_list[7] = "r"

                if word_selector_stars == "k":
                    word_selector_stars_list[9] = "k"

                if guesses_left == 10:
                    print("You did it in first Try. You must have cheated.")

    guessed_left = 10

"""
A General guide for Hangman
1. Make a work bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already used
5. Create the win condition
"""
