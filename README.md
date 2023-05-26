# Computer Vision RPS
>In this project the main goal is to simulate the classic game Rock, Paper, Scissors. You will play against the computer by showing the camera your choice (rock, paper or scissors)

## Milestone 1

-In this milestone I created the model which will allow the user to use their camera to pick between the 3 options (rock, paper or scissors) in front of the camera and that choice to be recognised by the code
- THe model was done using the website https://teachablemachine.withgoogle.com/train/image
- Using that tool I managed to train the computer to recognise signs and assign them to one of the options (rock, paper or scissors)
- After training the model I dowloaded it and added to my project folder and push the changes to GitHub

## Milestone 2

- In this milestone I created the logic for the game by defining the function`get_computer_choice` that chooses at random for the computer one option and `get_user_choice` which asks the user to pick between rock, paper or scissors
- I also defined the function `get_winner` which takes two arguments as an input, the user choice and the computer choice, and then works out who won the round
- Finally, I created the function `play` to play the game, this function calls the function `get_winner` and takes as an input the boht functions `get_computer_choice` and `get_user_choice`

## Milestone 3

- In this milestone, instead of the user manually entering their input, the user choice is determined by what hey show to the camera and the prediction with the highest probability of happening based on what they are showing.
- The function `get_prediction` starts the camera and tells the user if the press the 'w' key the countdown will start for them to show their input to the camera and when they are happy with the input they can press 'q' to exit the while loop and close the camera. Then the function pics the highest probability in the last array and based in the index of that max value it translate it to rock, paper, scissors or anything.
- I modified the function `get_winner` to add a point to either the user or the computer, depending who won the round.
- Finally, inside a while loop, the function `play` runs until either the user or the computer has 3 points.