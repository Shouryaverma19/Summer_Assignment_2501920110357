import random

target = random.randint(1, 100)
guess = 0

while guess != target:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < target:
        print("Too low! Try again.")
    elif guess > target:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")