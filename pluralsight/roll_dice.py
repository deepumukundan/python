import random

print("Rolling the dice...")
roll = random.randint(1, 6)
guess = int(input("Guess the number (1-6): "))

if guess == roll:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {roll}.")