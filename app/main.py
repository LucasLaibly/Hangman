import sys
import hangman

wordToGuess = ""
letter = ""

def run():

    # gets the user to enter a number
    while True:
        try:
            number = int(input("Please enter a number (0-3): "))
            break
        except:
            print("Not a valid value, try again")

    # build the game around the number
    game = hangman.Game(number)

    # retrieve the hidden word
    global wordToGuess
    wordToGuess  = game.guessWord(number)

    # prompt for user to begin gameplay
    global letter
    letter = game.promptForGuess()

if __name__ == "__main__":
    run()