import random

class Computer:
    '''
    Class to create a computer object

    Class dedicated to the computer.
    The only method will be the 'get_prediction' method, that at random one of the following choices:
    rock, paper or scissors, and returns it as the output of the function.
    '''

    
    def get_computer_choice(self):
        '''
        This function gets the computer choice at random between "Rock, Paper or Scissors".

        The purpose of this function is for the computer to select at random one option
        between Rock, Paper or Scissors so it can then be returned by the function.
        '''
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(computer_choice)
        return computer_choice