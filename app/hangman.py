import sys
import collections

BODY = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
STATE = []
COUNTER = 0
WORD = ""
usedLetters = []
NEWGUESS = ""

class Game:

    number = 0
    word = ""

    # constructor
    def __init__(self, number):
        self.number = number

    # array of words that the user can get assigned
    def guessWord(self, number):
        global WORD

        words = ["pink", "blue", "green", "white"]

        WORD = words[number]

        return words[number]

    # ask the user for their guess
    def promptForGuess(self):
        global usedLetters
        global NEWGUESS
        
        try:
            NEWGUESS = input("Please enter your guess: ")
            self.validateGuess(usedLetters, NEWGUESS)
        except NameError:
            pass

        return NEWGUESS

    # validate the guess to see if it has already been used
    def validateGuess(self, usedLetters, newLetter):
        newLetter = newLetter.lower()
        
        # letter in word and unique
        if(newLetter not in usedLetters and newLetter in WORD):
            usedLetters.insert(len(usedLetters), newLetter)
            return False

        # letter is not in the word but unique    
        elif (newLetter not in usedLetters and newLetter not in WORD):
            usedLetters.insert(len(usedLetters), newLetter)
            self.addLimb(WORD, newLetter)
            return False

        # user is a genius: letter not in word and has been used    
        else:
            self.addLimb(WORD, newLetter)
            print("not only have you used that letter, it is also not in the word.")
            return True

    # for each wrong guess, add a limb
    def addLimb(self, word, letter):
        global COUNTER
        global STATE
        
        if ( letter not in word ):
            STATE.insert(COUNTER, BODY[COUNTER])
            print(STATE)
        
        COUNTER += 1
        return True

    # check progress of current game
    def progress(self):
        return STATE

    # check the current used letters
    def usedLetterList(self):
        return usedLetters
    
    # if the user knows the word: allow for a total guess [ ONCE ]
    def coinFlip(self, chance):
        if chance == WORD:
            return True
        else:
            return False

    # end game if the user has completed the body
    def kill(self):
        if (STATE == BODY):
            return True
        else:
            return False