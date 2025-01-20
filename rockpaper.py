import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print("Rock, Paper, Scissors - Shoot!")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice == computer_choice:
        print(f"Both chose {user_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")

rock_paper_scissors()
