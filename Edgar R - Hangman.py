import random
import string

lose_condition = 10

player_stop_playing = "False"

punctuation = string.punctuation

lowercase_letters = string.ascii_lowercase

uppercase_letters = string.ascii_uppercase

word_phrase_bank = ["Classwork", "Teenager", "Community", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]


def word_finder():
    print("You guess a letter right. The letter was %s." % word_guessed)
    if word_guessed == len(word_phrase_bank):
        word_phrase_bank = "google"


def letter_wrong():
    if wordguess != len(word_phrase_bank):
        word_phrase_bank = "guess"


while player_stop_playing != "True":
    word_selector = random.choice(word_phrase_bank)

    # word_converter = word_selector.punctuation()

    # print(word_converter)

    word_guessed = input("Guess the word ")

    word_guessed = word_guessed.lower()

    print(word_guessed)
    name = input("How")

"""
A General guide for Hangman
1. Make a work bank - 10 items
2. Pick a random item from the list
3. Hide the word (use *)
4. Reveal letters already used
5. Create the win condition

"""
