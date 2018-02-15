import random

guesses_left = 10

word_phrase_bank = ["Classwork", "Train", "Computer", "Blackjack", "NaNi", "Firefox", "Lucky", "Window",
                    "Terraria", "Minecraft"]

letter_in_words = 0

guessed_words = []

word_selected = random.choice(word_phrase_bank)

word_selected = word_selected.lower()

print("Lets play Hangman. To play, you just have to guess a letter. You have 10 chances to guess the word.")

while guesses_left > 0:
    output = []

    for letter in word_selected:
        if letter in guessed_words:
            output.append(letter)
            guesses_left += 1

        else:
            output.append("*")

    hidden_word = "".join(output)

    print(hidden_word)

    print("You have %s guesses left." % guesses_left)

    print("These are the words you have guessed %s " % guessed_words)

    letter_guessed = input("Guess the letter. ")

    guesses_left -= 1

    lowercase_guess = letter_guessed.lower()

    guessed_words.append(lowercase_guess)

    correct_word = list(word_selected)

    if letter_guessed == word_selected:
        print("You win.")
        guesses_left = -0

    if output == word_selected:
        print("You win")
        exit(0)
print("Game Over")
