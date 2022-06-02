# WORD FINDING GAME

## Overview
The word finding game is based on two games. Wordle and Quordle.For each game mode, two language options are available. Wordle has 3 different modes. These modes are 4,5,6 lettered wordles. In Wordle, the main purpose of the game is to find a secret word. By trying new words, the player gets information about the position of the letters. If a letter is in the secret word and in the correct position, the letter is highlighted with green. If a letter is in the word but in the wrong position, the letter is highlighted with yellow. If a letter is not in a word, it's printed with black.
For Quordle, there are 4 secret words. With 9 guesses, the player is trying to find all four secret words. Each time a guess is made, the results are shown for all four words.
## Project Explanation
I used python classes to create a wordle class. This class has functions to calculate the maximum attempt number,add attempt to the attempts list,check whether if the puzzle is solved,check if the maximum attempt number is exceeded, a dictionary creator for the colors of the letters and a function called "wordle" to take guess as input, print colorful letters. I created another python script called "game.py".In this file I created a function to let the player choose the game mode,a function to create Wordle objects according to the chosen mode,a quordle function to iteratively create 4 wordle objects.



## How to run
To run the code, Colorama package should be installed. tr.txt,trr.txt,wordlist.txt files should be in the same directory. wordle.py file consists of the Wordle class, game.py is to run the game interface.

