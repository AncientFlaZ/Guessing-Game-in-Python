import random
number = random.randrange(1,1000)
guess = int (input("Guess number between 1 to 1000: "))

while guess != number:
    if guess < number:
        print("Guess Higher Number: ")
        guess = int (input("\n\n\nGuess number between 1 to 1000: "))
    else:
        print("Guess lower Number: ")
        guess = int (input("\n\n\nGuess number between 1 to 1000: "))
print("Corrent Number")
