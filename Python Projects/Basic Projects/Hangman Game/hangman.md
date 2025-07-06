# Hangman Game 

## Code Explanation:


1. Importing the random and time libraries:

# Initial Steps to invite in the game:
```python
import random
import time
print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)
```
- We define the main function that initializes the arguments: global count, global display, global word, global already_guessed, global length and global play_game. They can be used further in other functions too depending on how we want to call them.

- Words_to_guess: Contains all the Hangman words we want the user to guess in the game.
Word: we use the random module in this variable to randomly choose the word from words_to_guess in the game.

- Length: len() helps us to get the length of the string.

- Count: is initialized to zero and would increment in the further code.

- Display: This draws a line for us according to the length of the word to guess.

- Already_guessed: This would contain the string indices of the correctly guessed words.