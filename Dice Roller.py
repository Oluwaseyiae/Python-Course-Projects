import random

print("WELCOME! to this Dice game")
print("---------------------------")

while True:
    print("How many dice would you like to roll? ")

    while True:
        try:
            numberPicked = int(input("Type an integr between 1 to 10: "))
            if (numberPicked > 0 and numberPicked <=10):
                break
            else:
                print("Invalid input! Please try again")
        except:
            print("Please provide a valid integer")

    def rolldice(ammountOfDice):
        totalSum  = 0
        possibleFaces = [1,2,3,4,5,6]
        for die in range(ammountOfDice):
            roll = random.choice(possibleFaces)
            print("Die ", die +1, ": ", roll)
            totalSum += roll
            average = totalSum / ammountOfDice
        print("Total sum: ", totalSum)
        print("Average roll ", int(average))


    rolldice(numberPicked)