import random
from hangman_art import HANGMANPICS
from hangman_wordlist import word_list

rand_word = random.choice(word_list)
print(rand_word)

display_list = []
for letter in rand_word:
    display_list.append("_")

print(display_list)

wrong_guess = 7
while display_list.__contains__("_") and wrong_guess > 0:
    input_letter = input("Guess a letter: ").lower()

    if input_letter not in rand_word:
        print(HANGMANPICS[len(HANGMANPICS) - wrong_guess])
        wrong_guess -= 1
        print(display_list)
    else:
        for index, letter in enumerate(rand_word):
            if input_letter == letter:
                display_list[index] = input_letter
        print(display_list)

print("Thanks for playing the game!")


