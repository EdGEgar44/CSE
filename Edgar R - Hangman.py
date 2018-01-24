import random
import string

guesses_left = 10

player_stop_playing = "False"

punctuation = string.punctuation

lowercase_letters = string.ascii_lowercase

uppercase_letters = string.ascii_uppercase

word_phrase_bank = ["Classwork", "Train", "Computer", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]

guessed_words = []


while player_stop_playing != "True":

    play_a_game = input("Do you want to play a game of Hangman?(Yes or no) ")

    play_a_game = play_a_game.lower()

    while play_a_game == "yes" and guesses_left >= 0:

        word_selector = random.choice(word_phrase_bank)

        range_of_letter = len(word_selector)

        word_selector_stars = range_of_letter * "*"

        if word_selector == "Mr.Wiebe":
            word_selector_stars = "**.*****"

        print(word_selector_stars)

        word_selector = word_selector.lower()

        while guesses_left >= 0:

            print("These are the words you have guessed %s " % guessed_words)

            print("You have %s guesses left." % guesses_left)

            word_guessed = input("Guess the letter. ")

            word_guessed = word_guessed.lower()

            if word_guessed != word_selector:
                word_guessed = guessed_words.append(word_guessed)
                guesses_left -= 1

            print(guessed_words)

            if word_guessed == word_selector:
                print("You got it right!")

                print("You have %s guesses left." % guesses_left)

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
