import random
import string

guesses_left = 10

alphabet = list(string.ascii_letters)

player_stop_playing = "False"

word_phrase_bank = ["Classwork", "Train", "Computer", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]

guessed_words = []

while player_stop_playing != "True":

    play_a_game = input("Do you want to play a game of Hangman?(Yes or no) ")

    play_a_game = play_a_game.lower()

    word_selected = random.choice(word_phrase_bank)

    while play_a_game == "yes" and guesses_left >= 0:

        range_of_letter = len(word_selected)

        word_selector_stars = range_of_letter * "*"

        word_selector_stars_list = list(word_selector_stars)

        if word_selected == "Mr.Wiebe":
            word_selector_stars = "**.*****"

        word_selected = word_selected.lower()

        word_selected = list(word_selected)

        while guesses_left >= 0:
            print("These are the words you have guessed %s " % guessed_words)

            print("You have %s guesses left." % guesses_left)

            print(word_selector_stars)

            print(word_selected)

            word_guessed = input("Guess the letter. ")

            word_guessed = word_guessed.lower()

            print(guessed_words)

            output = word_selected
        while word_guessed != word_selected or guesses_left <= 0:
            for letter in word_guessed:
                if letter in word_guessed:
                    output.append(word_guessed)
                else:
                    output.append("*")

            if word_guessed == word_selected:
                guesses_left = 0
                if guesses_left == 10:
                    print("You did it in first Try. You must have cheated.")

            if word_guessed != word_selected:
                word_guessed = guessed_words.append(word_guessed)
                print("Try again")
                guesses_left -= 1

    guessed_left = 10

"""
4. Reveal letters already used
"""
