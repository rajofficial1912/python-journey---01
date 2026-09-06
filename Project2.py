'''
Rock Paper Scissors Game

User can play against the computer. The game will continue until the user decides to quit.
 The program will keep track of the score and display it after each round.
'''
import random
items = ["rock", "paper", "scissors"]
score = {"user": 0, "computer": 0}

while True:
    user_input = input("Enter your move (rock, paper, scissors), or quit: ").lower()

    if user_input == "quit":
        break
    if user_input not in items:
        print("Invalid move. Please choose rock, paper, or scissors.")
        continue

    computer_input = random.choice(items)

    print(f"Your move: {user_input}")
    print(f"Computer move: {computer_input}")

    if user_input == computer_input:
        print("It is a tie!")
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        print("You win!")
        score["user"] += 1
    else:
        print("You lose!")
        score["computer"] += 1

    print(f"Score: User {score['user']} - Computer {score['computer']}")

print(f"Final score: User {score['user']} - Computer {score['computer']}")