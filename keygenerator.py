import random
import pygame
from pygame.locals import *
pygame.init()

# maybe use generator instead of list for the keys to save memory

class keygenerator():
    modes = {"upperCase": (65, 90),
             "allKeys": (32, 122),
             "lowerCase": (97, 122),
             "abc": (97, 122)}

    def __init__(self):
        self.mode = None
        self.keys = []


    def generateNewKeys(self):
        self.set_mode_keys()
        if self.mode != "abc":
            random.shuffle(self.keys) 

    def set_mode_keys(self):
        lower, upper = self.get_mode_limits()
        self.keys = [i for i in range(lower, upper)]

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

    def get_mode_name(self):
        return self.mode

    def get_mode_limits(self):
        limits = self.modes[self.mode]
        return limits

    def checkUpperKeys(self, key, mod):
        if key == self.getKey(0) + 32:
            return self.check_if_shift_down(mod)
        else: 
            self.check_if_shift_released(key)
    
    def check_if_shift_down(self, mod):
        if mod & pygame.KMOD_LSHIFT or mod & pygame.KMOD_RSHIFT:
            return True
        return False

    def check_if_shift_released(self, key):
        lshift = pygame.KMOD_LSHIFT
        rshift = pygame.KMOD_RSHIFT
        if key == lshift or key == rshift:
            return None
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
