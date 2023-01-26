import random
from Words import words
import string





def get_valid_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print("You've", lives, "left and have used this letters", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list), "\n")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print("You've already guessed this letter. Please try again!")

        else:
            print("Invalid character! Try again")

    if lives == 0:
        print("You died. The word was", word.upper())

    else:
        print("You guessed the word", word.upper(), ":)")


hangman()

Trial = input("Do you wish to play again?[Yes/ No]: ").lower()

while Trial == "yes":
    hangman()
