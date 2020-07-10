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
            random.shuffle(self.keys)
        else:
            # standard case just regular abc game
            self.keys = [i for i in range(97, 122)]

        print(self.keys)

    def getKey(self, num):
        if not self.keys:
            self.generateNewKeys()
        key = self.keys[num]
        return key

    def removeFirstKey(self):
        del self.keys[0]

    def getKeys(self):
        if not self.keys:
            self.generateNewKeys()
        return self.keys

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode

    def checkShift(self, mod):
        if mod & pygame.KMOD_LSHIFT or mod & pygame.KMOD_RSHIFT:
            return True
        return False

    def checkUpperKeys(self, key, mod):
        if key == self.getKey(0) + 32:
            return self.checkShift(mod)
        else: 
            # fixes so that the program don't quit if shiftkey is hit
            if key == 303 or key == 304:
                return None
            else:
                return False

    def checkLowerKeys(self, key):
        if key == self.getKey(0):
            return True
        return False

    def checkMods(self, key, mod):
        correctKey = None

        if self.mode is None:  # if something bugs and mode is none
            correctKey = self.checkLowerKeys(key)
        elif self.mode[0] == 65 and self.mode[1] == 90:  # checks upper
            correctKey = self.checkUpperKeys(key, mod)
        else:
            correctKey = self.checkLowerKeys(key)

        if correctKey is None:
            return False, False  # gameover, correctKey
        elif correctKey:
            return False, correctKey
        else:
            return True, correctKey
