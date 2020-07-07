import sys
import hangman

global wordToGuess

def run():
    while True:
        try:
            number = int(input("Please enter a number (0-3): "))
            break
        except:
            print("Not a valid value, try again")

    # gets the user to enter a number
    game = hangman.Game(number)

    # retrieve the hidden word
    wordToGuess = game.guessWord(number)

    # prompt for user to begin gameplay
    letter = game.promptForGuess()

if __name__ == "__main__":
    run()