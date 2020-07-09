from keygenerator import keygenerator
from gui import gui
import pygame
from pygame.locals import *
pygame.init()


class game():

    def __init__(self):
        self.keygenerator = keygenerator()
        self.gameOver = False
        self.modes = None
        self.points = 0
        self.setModes()
        self.gui = None
        self.clock = pygame.time.Clock()
        self.first = True
        self.totalTime = 0

    def getKey(self, num):
        return self.keygenerator.getKey(num)

    def setNewKeys(self):
        self.keygenerator.generateNewKeys()

    def getModes(self):
        return self.modes

    def setModes(self):
        self.modes = {"upperCase": (65, 90),
                      "allKeys": (1, 122),
                      "lowerCase": (97, 122)}

    def removeKey(self):
        self.keygenerator.removeFirstKey()
        if self.first:
            self.clock.tick()
            self.first = False
        self.clock.tick()
        self.totalTime += self.clock.get_time()
        print(self.totalTime / 1000)
        print(self.calculateWPM())

    def setCurrentMode(self, mode):

        try:
            if mode in self.modes:
                self.keygenerator.setMode(self.modes[mode])
        except NameError:
            print("Not a correct mode")

    def checkKeys(self, key, mod):
        self.gameOver, correctkey = self.keygenerator.checkKeys(key, mod)
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
        if self.totalTime != 0:
            cps = self.points // (self.totalTime / 1000)
            wpm = cps * 60 / 5
            print(wpm)

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
