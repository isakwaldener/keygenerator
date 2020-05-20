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

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode

    def checkKeys(self, key, mod):
        rightkey = None
        if self.mode[0] == 65 and self.mode[1] == 90:
            print(key)
            if key == self.getKey(0) + 32:
                print("NICe")
                print(pygame.KMOD_SHIFT)

                if mod & pygame.KMOD_LSHIFT or mod & pygame.KMOD_RSHIFT:
                    print("UPper")
                    rightkey = True
                else:
                    rightkey = False
            else:
                if key == 303 or key == 304:
                    print("allal")
                    rightkey = None
                else:
                    rightkey = False
        else:
            if key == pygame.key.name(self.getKey(0)):
                rightkey = True
            rightkey = False

        if rightkey is None:
            return False, False# gameover, correctkey
        elif rightkey:
            return False, rightkey
        else:
            return True, rightkey

            