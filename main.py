import random

def play_game():
    choices = ['rock', 'scissors', 'paper']

    your_choice = input("Choose rock, scissors, or paper: ")
    computer_choice = random.choice(choices)

    print(f"Your choice: {your_choice}")
    print(f"Computer's choice: {computer_choice}")

    if your_choice in choices:
        if your_choice == computer_choice:
            print("It's a tie!")
        elif (
            (your_choice == 'rock' and computer_choice == 'scissors') or
            (your_choice == 'scissors' and computer_choice == 'paper') or
            (your_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
        else:
            print("Computer wins!")
    else:
        print("Invalid choice. Please enter 'rock', 'scissors', or 'paper'.")

play_game()