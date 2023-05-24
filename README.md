# Computer Vision RPS
>In this project the main goal is to simulate the classic game Rock, Paper, Scissors. You will play against the computer by showing the camera your choice (rock, paper or scissors)

## Milestone 1

-In this milestone I created the model which will allow the user to use their camera to pick between the 3 options (rock, paper or scissors) in front of the camera and that choice to be recognised by the code
- THe model was done using the website https://teachablemachine.withgoogle.com/train/image
- Using that tool I managed to train the computer to recognise signs and assign them to one of the options (rock, paper or scissors)
- After training the model I dowloaded it and added to my project folder and push the changes to GitHub

## Milestone 2

-In this milestone I created the logic for the game by defining the function`get_computer_choice` that chooses at random for the computer one option and `get_user_choice` which asks the user to pick between rock, paper or scissors
-I also defined the function `get_winner` which takes two arguments as an input, the user choice and the computer choice, and then works out who won the round
- Finally, I created the function `play` to play the game, this function calls the function `get_winner` and takes as an input the boht functions `get_computer_choice` and `get_user_choice`