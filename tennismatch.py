# tennismatch.py
from tennisplayer import Player

class TennisMatch:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.isOver():
            while not self.setOver():
                while not self.gameOver():
                    if self.server.winsServe():
                        self.server.incGScore()
                    else:
                        self.changeServer()
                        self.server.incGScore()
                        self.changeServer()
                self.server.resetGame()
                self.changeServer()
                self.server.resetGame()
            self.detwinner()
                
    def playDuce(self):
        pA,pB = 0,0
        while 1 == 1:
            if self.server.winsServe():
                pA += 1
            else: pB += 1
            if pA-pB == 2:
                self.server.incSetScore()
                break
            if pB-pA == 2:
                self.changeServer()
                self.server.incSetScore()
                self.changeServer()
                break
        return True

    def tieBreaker(self):
        while not self.gameOver():
            if self.server.winsServe():
                self.server.incGScore()
            else:
                self.changeServer()
                self.server.incGScore()
                self.changeServer()
        self.server.resetGame()
        self.changeServer()
        self.server.resetGame()
            

    def setadd(self):
        if self.playerA.getGameScore() == 1:
            self.playerA.incSetScore()
        else: self.playerB.incSetScore()
        return True

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()

    def detwinner(self):
        if self.playerA.getSetScore() == 6 or self.playerA.getSetScore() == 7:
            self.playerA.incSetWon()
        elif self.playerB.getSetScore() == 6 or self.playerB.getSetScore() == 7:
            self.playerB.incSetWon()

    def gameOver(self):
        if self.playerA.getGameScore() == 40 and self.playerB.getGameScore() == 40:
            return self.playDuce()
        elif self.playerA.getGameScore() == 1 or self.playerB.getGameScore() == 1:
            return self.setadd()
        else: return False

    def setOver(self):
        if self.playerA.getSetScore() == 6 and self.playerB.getSetScore() == 6:
            self.tieBreaker()
        elif (self.playerA.getSetScore() == 6 and self.playerB.getSetScore() != 5) \
             or (self.playerB.getSetScore() == 6 and self.playerA.getSetScore() != 5):
            return True
        elif self.playerA.getSetScore() == 7 or self.playerB.getSetScore() == 7:
            return True
        else:
            return False
            
    def isOver(self):
        if self.playerA.getSetsWon() == 3:
            self.playerA.incScore()
            return True
        elif self.playerB.getSetsWon() == 3:
            self.playerB.incScore()
            return True
        else: return False

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA
