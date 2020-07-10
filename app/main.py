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

    while True:
        global letter
        global wordToGuess

        if (game.kill):
            print("you lose.")
            return

        action = input("Please select your action. Enter (1) for continue, (2) for making your final guess: ")

        if ( action == "1"):
            print("\n")
        else:
            # the end of the game
            solution = input("What is your final guess? ")
            result = game.coinFlip(solution)
            if(result):
                print("you win. neato.")
                return
            else:
                print("you lost. big sad.")
                break

        # retrieve the hidden word
        wordToGuess  = game.guessWord(number)

        # prompt for user to begin gameplay
        letter = game.promptForGuess()


if __name__ == "__main__":
    run()