import random


class Scoreboard:
    '''
    This class manages the score and checks for a winner.

    The purpose of this class is to keep track of the score and the winner for each round of the game of rock
    paper, scissors. It does not have a class initializer as the scores are attributes of the user and computer
    classes.
    '''
    def __init__(self, computer_wins=0, user_wins = 0):
        '''
        Initializer of the class Computer.

        The only attribute is the computer score, pre set to 0 at the beginning.
        '''
        self.computer_wins = computer_wins
        self.user_wins = user_wins

    def get_winner(self, computer_choice, user_choice):
        '''
        This function determines who is the winner of the round, the machine or the user.

        The purpose of this function is to define the logic of the game and to determine who is the winner,
        if the user or the computer. This function takes as input both user and computer choices (you can pass both 
        functions as they return the computer and user choice) and compares them against each other using every possible 
        scenario, and determines who is the winner of the round. This function prints if the user
        won, lost or it is a tie and it will add a point to the winner. The function does not return anything.
        '''

        if computer_choice == "rock" and user_choice == "scissors":
            print("You lost!")
            self.computer_wins += 1
        elif computer_choice == "rock" and user_choice == "paper":
            print("You won!")
            self.user_wins += 1
        elif computer_choice == "rock" and user_choice == "rock":
            print("It is a tie!")
        elif computer_choice == "paper" and user_choice == "scissors":
            print("You won!")
            self.user_wins += 1
        elif computer_choice == "paper" and user_choice == "paper":
            print("It is a tie!")
        elif computer_choice == "paper" and user_choice == "rock":
            print("You lost!")
            self.computer_wins += 1
        elif computer_choice == "scissors" and user_choice == "rock":
            print("You won!")
            self.user_wins += 1
        elif computer_choice == "scissors" and user_choice == "paper":
            print("You lost!")
            self.computer_wins += 1
        elif computer_choice == "scissors" and user_choice == "scissors":
            print("It is a tie!")
