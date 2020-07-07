import sys
import hangman

wordToGuess = ""

def run():
    while True:
        try:
            number = int(input("Please enter a number: "))
            break
        except:
            print("Not a valid interger value, try again")

    game = hangman.Game(number)
    wordToGuess = game.guessWord(number)

if __name__ == "__main__":
    run()