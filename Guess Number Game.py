import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("You didn't insert a number")
        quit()
else:
    print("Insert a number next time")
    quit()
    
random_number = random.randint(0, top_of_range)

guesses = 0
while True :
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time")
        continue
    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
           print("The number is grater than the Base Number, try again")
    else:
      print("You didn't get it")
print (f"You got it in {guesses} guesses")
