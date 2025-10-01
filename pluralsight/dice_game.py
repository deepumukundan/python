import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(f"{player1} rolled a {roll1}")
    print(f"{player2} rolled a {roll2}")

    if roll1 > roll2:
        print(f"{player1} wins!")
    elif roll2 > roll1:
        print(f"{player2} wins!")
    else:
        print("It's a tie!")

main()