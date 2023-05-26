import random
import camera_rps

computer_wins = 0
user_wins = 0

def get_computer_choice():
    '''
    This function gets the computer choice at random between "Rock, Paper or Scissors".

    The purpose of this function is for the computer to select at random one option
    between Rock, Paper or Scissors so it can then be returned by the function.
    '''
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(computer_choice)
    return computer_choice


def get_user_choice():
    '''
    This function asks the user to input their choice between "Rock, Paper or Scissors".

    The purpose of this function is to ask the user to manually input their choice
    between Rock, Paper or Scissors, lower case it, so it can then be returned by the function.
    '''
    user_choice = input("Please pick between Rock, Paper or Scissors ").lower()
    return user_choice


def get_winner(computer_choice, user_choice):
    '''
    This function determines who is the winner of the round, the machine or the user.

    The purpose of this function is to define the logic of the game and to determine who is the winner,
    if the user or the computer. This function takes as input both user and computer choices (you can pass both 
    functions as they return the computer and user choice) and compares them against each other using every possible 
    scenario, and determines who is the winner of the round. This function prints if the user
    won, lost or it is a tie and it will add a point to the winner. The function does not return anything.
    '''
    global computer_wins
    global user_wins
    if computer_choice == "rock" and user_choice == "scissors":
        print("You lost!")
        computer_wins += 1
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
        user_wins += 1
    elif computer_choice == "rock" and user_choice == "rock":
        print("It is a tie!")
    elif computer_choice == "paper" and user_choice == "scissors":
         print("You won!")
         user_wins += 1
    elif computer_choice == "paper" and user_choice == "paper":
        print("It is a tie!")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You lost!")
        computer_wins += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
        user_wins += 1
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You lost!")
        computer_wins += 1
    elif computer_choice == "scissors" and user_choice == "scissors":
        print("It is a tie!")


def play():
    '''
    This function runs the game.

    The purpose of this function is to run the game by calling the function `get_winner` which
    also calls the functions `get_computer_choice` and `get_prediction` (from the file camera_rps.py) 
    and prints if the user won, lost or it is a tie. It does not return anything.
    '''  
    get_winner(get_computer_choice(), camera_rps.get_prediction())


while True:
    play()

    if computer_wins == 3:
        print("Computer is the winner!")
        break
    elif user_wins == 3:
        print("You are the winner!")
        break