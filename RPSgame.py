import random

options = ["rock", "paper", "scissors"]

while True:
    choose = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").strip().lower()

    if choose == 'quit':
        print("Thanks for playing!")
        break
    elif choose not in options:
        print("Invalid choice. Please choose rock, paper, scissors or quit.")
        continue

    computer_choice = random.choice(options)
    print("Computer choice:", computer_choice)

    if choose == computer_choice:
        print("It's a tie!")
    elif (choose == "rock" and computer_choice == "scissors") or \
         (choose == "paper" and computer_choice == "rock") or \
         (choose == "scissors" and computer_choice == "paper"):
        print("You win!")
    elif (choose == "rock" and computer_choice == "paper") or \
         (choose == "paper" and computer_choice == "scissors") or \
         (choose == "scissors" and computer_choice == "rock") :
        print("you lose!")
    else:
        print("Invalid input. please try again.")