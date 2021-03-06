import sys
import hangman

wordToGuess = ""
letter = ""

def run():

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

    while True:
        global letter

        if (game.kill()):
            print("you lose.")
            return

        action = str(input("Please select your action. Enter (1) for continue, (2) for making your final guess, (3) for more options: "))
        
        if ( action == "1"):
            print("\n")
        elif ( action == "3"):
            game.options()
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
        
        # prompt for user to begin gameplay
        letter = game.promptForGuess()


if __name__ == "__main__":
    run()