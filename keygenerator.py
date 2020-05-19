import random
import pygame
from pygame.locals import *
pygame.init()


class keygenerator():

    def __init__(self):
        self.mode = None
        self.keys = []

    def generateNewKeys(self):

        if self.mode:
            self.keys = [i for i in range(self.mode[0], self.mode[1])]  # add mode values to this
        else:
            self.keys = [i for i in range(97, 122)]
        random.shuffle(self.keys)
        print(self.keys)

    def getKey(self, num):
        if not self.keys:
            self.generateNewKeys()
        key = self.keys[num]
        return key

    def removeFirstKey(self):
        del self.keys[0]

    def getKeys(self):
        return self.keys


    """def generateNewKey(self):

        if self.mode is None:
            key = randint(97, 122)
        else:
            key = randint(self.mode[0], self.mode[1])

        print(key)
        self.currentKey = key

    def getKey(self):
        if self.currentKey is None:
            self.generateNewKey()
        return self.currentKey"""

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode
