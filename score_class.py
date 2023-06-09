import random
import cv2
from keras.models import load_model
import numpy as np
import time


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


    def get_prediction(self):
        '''
        This method translates the sign the user is doing to the camera into a choice of rock, paper or scissors.

        The purpose of this function is to capture the input from the user using the camera of the computer.
        The user needs to press the key 'w' to start the three second count down. After the count down is over the user
        needs to show to the camera their choice in the form of a rock, a paper or a scissor. When done the user
        needs to press the "q" key to stop the video recording. The function will then pic the choice with biggest
        probability from the last array and convert it into the relevant choice (rock, paper, scissors or nothing).
        '''
        TIMER = 5
        model = load_model('keras_model.h5', compile=False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (0, 450)
            fontScale = 0.6
            color = (4, 4, 183)
            thickness = 2
            cv2.putText(frame, "Press the 'w' key to start the countdown and 'q' to exit", org, font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.imshow('frame', frame)

            k = cv2.waitKey(1)
            if k == ord('w'):
                prev = time.time()
                while TIMER >= 0:
                    ret, frame = cap.read()
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    org = (250, 250)
                    fontScale = 7
                    color = (255, 0, 0)
                    thickness = 4
                    cv2.putText(frame, str(TIMER), org, font, fontScale, color, thickness, cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    cv2.waitKey(1)
                    cur = time.time()
                    if cur-prev >= 1:
                        prev = cur
                        TIMER = TIMER - 1
            # Press q to close the window
            print(prediction)
            max_arr = np.max(prediction)
            print(max_arr)
            max_arr_loc = np.argmax(prediction)
            print(max_arr_loc)
            if k == ord('q'):
                break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()

        if max_arr_loc == 0:
            user_input = "rock"
        elif  max_arr_loc == 1:
            user_input = "scissors"
        elif  max_arr_loc == 2:
            user_input = "paper"
        else:
            user_input = "nothing"
        return user_input

    # print(get_prediction())


    def get_computer_choice(self):
        '''
        This method gets the computer choice at random between "Rock, Paper or Scissors".

        The purpose of this function is for the computer to select at random one option
        between Rock, Paper or Scissors so it can then be returned by the function.
        '''
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(computer_choice)
        return computer_choice


    def get_winner(self, computer_choice, user_choice):
        '''
        This method determines who is the winner of the round, the machine or the user.

        The purpose of this function is to define the logic of the game and to determine who is the winner,
        if the user or the computer. This function takes as input both user and computer choices (you can pass both 
        functions as they return the computer and user choice) and compares them against each other using every possible 
        scenario, and determines who is the winner of the round. This function prints if the user
        won, lost or it is a tie and it will add a point to the winner. The function does not return anything.
        '''
        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "rock" and user_choice == "scissors" or computer_choice == "paper" and user_choice == "rock" or computer_choice == "scissors" and user_choice == "paper":
            print("You lost!")
            self.computer_wins += 1
        elif computer_choice == "rock" and user_choice == "paper" or computer_choice == "paper" and user_choice == "scissors" or computer_choice == "scissors" and user_choice == "rock":
            print("You won!")
            self.user_wins += 1
