import sys

class Game:

    number = 0
    newGuess = ""
    usedLetters = []
    body = ["head", "body", "left arm", "right arm", "left leg", "right leg"]

    # constructor
    def __init__(self, number):
        self.number = number

    # array of words that the user can get assigned
    def guessWord(self, number):
        words = ["pink", "blue", "green", "white"]
        
        return words[number]

    # ask the user for their guess
    def promptForGuess(self):
        global newGeuss
        newGeuss = str(input("Please select a character guess: "))
        
        while True:
            if ( self.validateGuess(self.usedLetters, newGeuss) ):
                print(self.usedLetters)
                newGuess = str(input("Please enter a character you have not previously used: "))
            else:
                return newGuess


    # validate the guess to see if it has already been used
    def validateGuess(self, usedLetters, newLetter):
        
        if( newLetter.lower() not in usedLetters ):
            usedLetters.insert(len(self.usedLetters), newLetter)
            return True
        else:
            return False

    # break guessed word into an array
    # add character at the correct slot

    # for each wrong guess, add a limb

    # check progress of current game

    # if the user knows the word: allow for a total guess [ ONCE ]


