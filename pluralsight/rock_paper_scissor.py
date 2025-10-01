import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Enter rock, paper, or scissors: ").lower()

if computer_choice == user_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif (computer_choice == "rock" and user_choice == "scissors") or \
     (computer_choice == "paper" and user_choice == "rock") or \
     (computer_choice == "scissors" and user_choice == "paper"):
    print(f"You lose! {computer_choice} beats {user_choice}.")      
else:
    print(f"You win! {user_choice} beats {computer_choice}.")