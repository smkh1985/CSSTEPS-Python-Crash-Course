import random


def play():
    secret = random.randint(1, 20)
    tries = 0
    while True:
        guess = int(input("Guess a number from 1 to 20: "))
        tries += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {tries} tries!")
            break
