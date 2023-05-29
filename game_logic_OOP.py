from computer_class import Computer
from user_class import User
from score_class import Scoreboard

computer = Computer()
user = User()
score_user = Scoreboard()
score_computer = Scoreboard()



def play():
    '''
    This function runs the game.

    The purpose of this function is to run the game by calling the function `get_winner` which
    also calls the functions `get_computer_choice` and `get_prediction` (from the file camera_rps.py) 
    and prints if the user won, lost or it is a tie. It does not return anything.
    '''  
    score_user.get_winner(computer.get_computer_choice(), user.get_prediction())


while True:
    play()

    if score_computer.computer_wins == 3:
        print("Computer is the winner!")
        break
    elif score_user.user_wins == 3:
        print("You are the winner!")
        break