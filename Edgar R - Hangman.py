import random
import string

lose_condition = 10

word_phrase_bank = ["classwork", "teenager", "community", "Blackjack", "google", "firefox", "lucky", "window", "terraria",
             "mr.wiebe", "mining diamonds", "uganda warrior", "the queen", "hangman is the best", "bee movie"]

word_selector = random.randint(len(word_phrase_bank))

print(word_selector)

"""
A General guide for Hangman
1. Make a work bank - 10 items
2. Pick a random item from the list
3. Hide the word (use *)
4. Reveal letters already used
5. Create the win condition

"""
