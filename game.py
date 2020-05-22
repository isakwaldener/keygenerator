from keygenerator import keygenerator
import pygame
from pygame.locals import *
pygame.init()


class game():

    def __init__(self):
        self.keygenerator = keygenerator()
        self.gameOver = False
        self.modes = None
        self.points = 0

    def getKey(self, num):
        return self.keygenerator.getKey(num)

    def setNewKeys(self):
        self.keygenerator.generateNewKeys()

    def getModes(self):
        return self.modes

    def setModes(self):
        self.modes = {"upperCase": (65, 90), "allKeys": (1, 122)}

    def removeKey(self):
        self.keygenerator.removeFirstKey()

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
