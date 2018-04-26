# tennisplayer.py
from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        #matches won
        self.score = 0
        #game score - 15,30,40,1
        self.gscore = 0
        #set score - amount out of 6
        self.setscore = 0
        # sets won - out of 3
        self.setswon = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a pouint to this player's score
        self.score = self.score + 1

    def getScore(self):
        # Return this player's current score
        return self.score

    def getGameScore(self):
        return self.gscore

    def resetGame(self):
        self.gscore = 0

    def incSetScore(self):
        self.setscore += 1

    def getSetScore(self):
        return self.setscore

    def incSetWon(self):
        self.setswon += 1

    def getSetsWon(self):
        return self.setswon

    def incGScore(self):
        if self.gscore == 0:
            self.gscore = 15
        elif self.gscore == 15:
            self.gscore = 30
        elif self.gscore == 30:
            self.gscore = 40
        elif self.gscore == 40:
            self.gscore = 1
