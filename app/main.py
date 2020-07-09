import sys
import hangman

wordToGuess = ""
letter = ""

def run():
    global letter
    global wordToGuess

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
    wordToGuess  = game.guessWord(number)

    # prompt for user to begin gameplay
    letter = game.promptForGuess()

    # the end of the game
    solution = input("What is your final guess? ")
    result = game.coinFlip(solution)

    if(result):
        print("you win. neato.")
    else:
        print("you lost. big sad.")


if __name__ == "__main__":
    run()