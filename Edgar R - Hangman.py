import random
import string

guessed_left = 10

player_stop_playing = "False"

punctuation = string.punctuation

lowercase_letters = string.ascii_lowercase

uppercase_letters = string.ascii_uppercase

word_phrase_bank = ["Classwork", "Teenager", "Community", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]

letters_words = ["google"]


while player_stop_playing != "True":

    play_a_game = input("Do you want to play a game of Hangman?(Yes or no) ")

    play_a_game = play_a_game.lower()

    if play_a_game == "yes" and guessed_left >= 0:

        word_selector = random.choice(word_phrase_bank)

        range(len(word_selector))

        word_selector = punctuation

        word_guessed = input("Guess the letter")

    guessed_left = 10

"""
A General guide for Hangman
1. Make a work bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed
4. Reveal letters already used
5. Create the win condition
"""
