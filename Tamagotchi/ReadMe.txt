This is Assignment 01 for COMP 3522 - OO Programming.

The project itself has two files named tamagotchi.py and game.py. The purpose of the tamagotchi file was to create the blueprint for what a tamagotchi is.
There are 4 other possible tamagotchi that extend this class. They all have their own versions of the speak() method that is abstract but most of the methods were able to 
be created within the Tamagotchi class. The Egg class's purpose is to use the created tamagotchi pokemon to randomly "hatch" them from an egg. It cannot exist on its own and 
needs Tamagotchi in order to be useful.

The other methods basically do what they are labeled to do.

Game class builds the "choices" that are available in the game and also house a timer method that allows the program to keep track of how long the game has been running
for in order to calculate the decay rates.

When running the game, it should function normally. Inputting random keyboard characters will result in a error message but the game will continue until you select a proper
input. The game can continue even after the pokemon die. You could 1. spawn a new one or 2. exit the game. You can exit the game at any time too by entering "4".


Benson Wang
A01045793