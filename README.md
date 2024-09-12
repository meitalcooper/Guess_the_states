# Guess the States - U.S. States Game


## Project Overview
"Guess the States" is an interactive educational game that helps users learn and memorize the 50 states of the United States.
The game is built using Python's turtle module and displays a blank map of the U.S., allowing users to input the names of states they know.
The goal is to correctly guess all 50 states.

If the user gives up, the game reveals the states they didn't know and saves them in a file called states_to_learn.csv.

## Features
- Interactive guessing game using the turtle graphics.
- Displays the correct states on a U.S. map as they are guessed.
- Marks unguessed states in red after the game ends.
- Saves the names of unguessed states into a CSV file for later review.

##  Technologies Used
- **Python**: The main language used.
-  **Turtle**: A graphical library used to display the U.S. map and interact with the user.
-  **Pandas**: Used to read the CSV file containing the coordinates and names of the states and to write missing states into a CSV file.
- **CSV**: For handling data related to U.S. states and storing unguessed states.


# How to Play
1. Once you start the game, a blank U.S. map will appear.
2. Type the names of U.S. states into the input box. Correct guesses will be displayed on the map.
3. To exit the game, type Exit. The unguessed states will be displayed on the map in red.
4. A states_to_learn.csv file will be generated, listing the states you missed during the game.

   
 # Example of Gameplay
- The game prompts the user to guess a state's name.
- For each correct guess, the state is displayed on the map.
- If the user types "Exit", the game ends and displays the unguessed states on the map in red.
