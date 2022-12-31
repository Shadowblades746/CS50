import random

while True:
    level = input("Level: ")
    if not int(level.isnumeric()) or int(level) <= 0:
        continue
    else:
        break

number = random.randint(1, int(level))

while True:
    guess = input("Guess: ")
    if not int(guess.isnumeric()) or int(guess) < 0:
        continue
    else:
        if int(guess) < number:
            print("Too small!")
        elif int(guess) > number:
            print("Too large!")
        else:
            print("Just right!")
            break
