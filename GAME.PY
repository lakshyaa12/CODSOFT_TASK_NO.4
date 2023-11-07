print("Welcome to my codsoft internship project task-4 by LAKSHYA AGARWAL")
print("ROCK PAPER AND SCISSORS GAME")
print("*******************************************************************")
import random

def cpu():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def user():
    while True:
        player = input("Please enter your Choice: Rock, Paper, or Scissors: ").lower()
        if player in ["rock", "paper", "scissors"]:
            return player
        else:
            print("Invalid Input")

def win(U_choice, C_choice):
    if (U_choice == "rock" and C_choice == "scissors") or (U_choice == "scissors" and C_choice == "paper") or (U_choice == "paper" and C_choice == "rock"):
        return "You win :)"
    elif U_choice == C_choice:
        return "Dude, It's a tie!"
    else:
        return "You Lose :("

while True:
    U_score = 0
    C_score = 0
    rounds = 0

    print("Welcome to the Rock, Scissors, Game! Are you ready to rock and roll?")

    while True:
        U_choice = user()
        C_choice = cpu()

        print(f"You chose: {U_choice}")
        print(f"Computer chose: {C_choice}")

        result = win(U_choice, C_choice)
        print(result)

        if "You win :)" in result:
            U_score += 1
        elif "You Lose" in result:
            C_score += 1
        rounds += 1
        print(f"POINTS - USER: {U_score}, COMPUTER: {C_score}")
        
        play_again = input("Want to play again? (Yes/No): ").strip().lower()
        if play_again != "yes":
            break

    print(f"Total Rounds: {rounds} \nUser: {U_score} \nComputer: {C_score}")
    if U_score > C_score:
        print("You win!")
    else:
        print("See you next time :)")

    replay = input("Do you want to start a new game? (Yes/No): ").strip().lower()
    if replay != "yes":
        break
