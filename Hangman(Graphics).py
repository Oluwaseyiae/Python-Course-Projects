import random
from Words import words
import string




print("Welcome to Hangman Game")
print("-----------------------")


def get_valid_word(words):
    word = random.choice(words)
    for i in word:
        print(" ", end=" ")
    return word.upper()


# Game bod
 # Graphics section | The hangman graphic process

def graphics(missed):
    if (missed == 0):
        print("\n+-----+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 1):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 2):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print(" |    |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 3):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print("/|    |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 4):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 5):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("/     |")
        print("      |")
        print("      |")
        print("    ===")
    elif (missed == 6):
        print("\n+-----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("/ \   |")
        print("      |")
        print("      |")
        print("    ===")
    else:
        pass

# Functionalities Section
def print_word():
    current_word = get_valid_word(words)
    word_letters = set(current_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6


    print("\nYou have 6 lives")
    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else "_" for letter in current_word]
        print("Current word: ", " ".join(word_list), "\n")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                miss = 6 - lives
                graphics(miss)
                print("Letter is not in the word")
                print("You've", lives, "left and have used these letters: ", " ".join(used_letters))
        elif user_letter in used_letters:
            print("You've already guessed this letter. Please try again!")

        else:
            print("Invalid character! Try again")

    if lives == 0:
            print("You died. The word was", current_word.upper())

    else:
            print("You guessed the word", current_word.upper(), ":)")


print_word()

Trial = input("Do you wish to play again?[Yes/ No]: ").lower()

while Trial == "yes":
    print_word()