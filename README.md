# Computer Vision RPS

## Introduction
The main goal for this project is to simulate the classic game Rock, Paper, Scissors. You will:
- Play against the computer.
- Show to the camera your choice (rock, paper or scissors).
- Wait for the program to decide who is the winner.
- Need to score 3 points to win.

If you are not familiar with the game, you can read about it here: https://en.wikipedia.org/wiki/Rock_paper_scissors

## Usage

- Go to the file `game_logic_OOP.py` to start the game.
- Start a new terminal and type `python game_logic_OOP.py`
- Press `w` to start the countdown and when it reaches 0, show your pick to the camera for 2 seconds (the longer you show your choice to the camera the more accurate the prediction will be)
- Enjoy the game!

## Documentation

### 1. The files:
This repository contains several files:
1. `game_logic_OOP.py`: Runs the game.
2. `score_class.py`: Contains the class with the necessary attributes and methods for the code to work.
3. `keras.model.h5`: Contains the code that converts the user input into the camera into a string
4. `labels.txt`: Contains the possible options for the user: Rock, Paper, Scissors or Nothing
5.`README.md`: This file which contains all the explanation for the code.


### 2. Modules used:

This program uses different modules, briefly explained below:
1. Random: allows us to pick random values within a range or from an iterable object. You can find more information [here](https://docs.python.org/3/library/random.html)
2. cv2: used to initialize and access the camera in your computer. You can find more information [here](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html) 
3. keras.models: a neural network Application Programming Interface (API) for Python that is tightly integrated with TensorFlow, which is used to build machine learning models. You can find more information [here](https://keras.io/api/models/model/)
4. numpy:  is a python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. You can find more information [here](https://numpy.org/doc/stable/#)
5. time: this module provides various time-related functions. You can find more information [here](https://docs.python.org/3/library/time.html)

### 3. How to initialize a `Scoreboard` object to start the game

There is only one class in this program that contains several methods. Those methods and the class are listed below:

```
score = Scoreboard()
```

This will create the object for you. This class has the user score and the computer score as initializers, named `user_wins` and `computer_wins`, respectively. This object will track the score in the game to determine the winner.


### 4. Method 1: `get_prediction`

When this method is called it opens the user's webcam and displays a message to the user, to press `w` to start the countdown and to pres `q` to exit the camera. This method capture the user choice (rock, paper or scissor) and will return the user choice as a string. It is based on getting the index with the higher value in the vector `prediction` and interpreting the choice that is linked to an specific position in the vector.

```
def get_prediction(self):
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
```

### 5. Method 2: `get_computer_choice`

This method uses the random module (see section 2) to pick a random value between rock, paper or scissors for the computer pick and returns that pick.

```
def get_computer_choice(self):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(computer_choice)
    return computer_choice
```
### 6. Method 3: `get_winner`

This method takes as input both methods `get_prediction` and `get_computer_choice` and determines who is the winner.

```
    def get_winner(self, computer_choice, user_choice):

        if computer_choice == user_choice:
            print("It is a tie!")
        elif computer_choice == "rock" and user_choice == "scissors" or computer_choice == "paper" and user_choice == "rock" or computer_choice == "scissors" and user_choice == "paper":
            print("You lost!")
            self.computer_wins += 1
        elif computer_choice == "rock" and user_choice == "paper" or computer_choice == "paper" and user_choice == "scissors" or computer_choice == "scissors" and user_choice == "rock":
            print("You won!")
            self.user_wins += 1
```

### 7. The `play` function:

This function calls the `get_winner` method from the Scoreboard class and adds as input the methods `get_computer_choice` and `get_prediction` so this will activate the camera for the user to show his choice, it will pick a random option for the computer and will compare the options to determine the winner.
To keep the game running smoothly until wither the player or the computer scores 3 points, it uses a while loop that runs until one of the scores is equals to 3.

```
while True:
    play()

    if score.computer_wins == 3:
        print("Computer is the winner!")
        break
    elif score.user_wins == 3:
        print("You are the winner!")
        break
```

