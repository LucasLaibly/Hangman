import sys

class Game:

    number = 0
    usedLetters = []
    limbs = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

    def __init__(self, number):
        self.number = number

    # array of words that the user can get assigned
    def guessWord(self, number):
        words = ["pink", "blue", "green", "white"]
        
        return words[number]

    # ask the user for their guess
    def promptForGuess(self):
        newGeuss = str(input("Please select a character guess: "))

        self.validateGuess(self.usedLetters, newGeuss)

    # validate the guess to see if it has already been used
    def validateGuess(self, usedLetters, newLetter):
        if( newLetter not in usedLetters ):
            usedLetters.insert(newLetter)
            return False
        else:
            return True

    # break guessed word into an array
    # add character at the correct slot

    # for each wrong guess, add a limb

    # check progress of current game

    # if the user knows the word: allow for a total guess [ ONCE ]


