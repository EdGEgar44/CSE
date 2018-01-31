import random
import string

guesses_left = 10
player_stop_playing = "False"

word_phrase_bank = ["Classwork", "Train", "Computer", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Mr.Wiebe"]

guessed_words = []

output = []

word_selected = random.choice(word_phrase_bank)

word_selected = word_selected.lower()

print("Lets play Hangman. To play, you just have to guess a letter. You have 10 chances to guess the word.")

letter_guessed = input("Guess the letter. ")

guessed_words.append(letter_guessed)

while guesses_left >= 0:

    for letter in word_selected:
        if letter in letter_guessed:
            output.append(letter)
            guesses_left += 1
        else:
            output.append("*")

    hidden_word = " ".join(output)

    guesses_left -= 1

    print("You have %s guesses left." % guesses_left)

    print("These are the words you have guessed %s " % guessed_words)

    print(word_selected)

    print(hidden_word)

    asked_letter = input("Guess the letter. ")

    guessed_words.append(letter_guessed)

    asked_letter_lower = asked_letter.lower()

    correct_word = list(word_selected)

    if letter_guessed != output:
        print("Try again")

"""
4. Reveal letters already used
"""
