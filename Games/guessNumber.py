import random

print("Welcome to the guess number game.")
target = random.randint(0,10)

for x in range(4):
    print(4-x , 'attempts left')
    guess = input("Guess a number between 0-10: ")
    if int(guess) == target:
        print("well done")
        print("you have", 4-x ,"points")
        break
    elif int(guess) > target:
        print("too high")
    elif int(guess) < target:
        print("too low")
