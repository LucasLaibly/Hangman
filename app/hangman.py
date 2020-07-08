import sys

class Game:

    number = 0
    newGuess = ""
    word = ""
    usedLetters = []

    body = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
    gameState = []
    counter = 0

    # constructor
    def __init__(self, number):
        self.number = number

    # array of words that the user can get assigned
    def guessWord(self, number):
        words = ["pink", "blue", "green", "white"]

        global word
        word = words[number]

        return words[number]

    # ask the user for their guess
    def promptForGuess(self):
        global newGeuss
        newGeuss = str(input("Please select a character guess: "))
        
        if ( self.validateGuess(self.usedLetters, newGeuss) ):
            print(self.usedLetters)
            newGuess = str(input("Please enter a character you have not previously used: "))
        
        return newGeuss

    # validate the guess to see if it has already been used
    def validateGuess(self, usedLetters, newLetter):
        
        if( newLetter.lower() not in usedLetters ):
            usedLetters.insert(len(self.usedLetters), newLetter)
            
            return False
        else:
            return True

    # for each wrong guess, add a limb
    def addLimb(self, word, letter):
        count = self.counter
        if ( letter not in word ):
            gameState = gameState.insert(count+1, self.body[count])
        return True

    # check progress of current game

    # if the user knows the word: allow for a total guess [ ONCE ]