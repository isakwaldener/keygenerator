from keygenerator import keygenerator
from gui import gui
import pygame
from pygame.locals import *
pygame.init()


class game(keygenerator):

    def __init__(self):
        keygenerator.__init__(self)
        self.gameOver = False
        self.points = 0
        self.gui = None
        self.clock = pygame.time.Clock()
        self.first = True
        self.total_time = 0

    def setNewKeys(self):
        self.generateNewKeys()

    def getModes(self):
        return self.modes

    def removeKey(self):
        self.removeFirstKey()
        self.update_clock()

    def update_clock(self):
        self.check_if_first()
        self.clock.tick()
        self.total_time += self.clock.get_time()
    
    def check_if_first(self):
        if self.first:
            self.clock.tick()
            self.first = False

    def setCurrentMode(self, mode):
        if mode in self.modes:
            self.setMode(mode)
        else:
            print("Not a correct mode")

    def checkKeys(self, key, mod):
        self.gameOver, correctkey = self.checkMods(key, mod)
        if correctkey:
            self.setPoints(1)
        return correctkey
        
    def getGameover(self):
        return self.gameOver

    def setGameover(self, gameOver):
        self.gameOver = gameOver

    def setPoints(self, point):
        self.points += point

    def getPoints(self):
        return self.points

    def calculateWPM(self):
        wpm = 0
        if self.total_time != 0:
            cps = self.points // (self.total_time / 1000)
            wpm = cps * 60 / 5
            print(wpm)
        return wpm

    def getWPM(self):
        return self.calculateWPM()

    def getTotalTimeInSec(self):
        return self.total_time / 1000  # convert ms to s

    def createGame(self, mode):
        self.setCurrentMode(mode)
        self.gui = gui(self)
        self.gameLoop()

    def gameLoop(self):
        while not self.getGameover():

            for event in pygame.event.get():
                if event.type is QUIT:
                    self.setGameover(True)

                if event.type == pygame.KEYUP:

                    if self.checkKeys(event.key, event.mod):
                        self.removeKey()

            self.gui.updateBoard()

        self.gui.drawEndScreen()

        while True:
            for event in pygame.event.get():
                if event.type is QUIT:
                    pygame.quit()
