import random
import pygame
from pygame.locals import *
pygame.init()

# maybe use generator instead of list for the keys to save memory

class keygenerator():

    def __init__(self):
        self.mode = None
        self.keys = []


    def generate_new_keys(self):
        self.set_mode_keys()
        self.check_if_shuffle()
    
    def check_if_shuffle(self):
        if self.mode.should_shuffle():
            random.shuffle(self.keys)

    def set_mode_keys(self):
        lower, upper = self.get_mode_limits()
        self.keys = [i for i in range(lower, upper)]

    def get_key(self, num):
        if not self.keys:
            self.generate_new_keys()
        key = self.keys[num]
        return key

    def remove_first_key(self):
        del self.keys[0]

    def get_keys(self):
        if not self.keys:
            self.generate_new_keys()
        return self.keys

    def set_mode(self, mode):
        self.mode = mode

    def get_mode_name(self):
        return self.mode

    def get_mode_limits(self):
        limits = self.mode.get_limits()
        return limits

    def check_if_correct_key(self, key, mod):
        if self.mode.get_name() == "upper":
            return self.check_upper_keys(key, mod)
        else:
            return self.check_lower_keys(key)

    def check_key_test(self, key, mod):
        if self.get_key(0) >= 32 and self.get_key(0) <= 90:
            return self.check_upper_keys(key, mod)
        else:
            return self.check_lower_keys(key)

    def check_upper_keys(self, key, mod):
        if key == self.get_key(0) + 32:
            return self.check_if_shift_down(mod)
        else: 
            return self.check_if_shift_released(key)
    
    def check_if_shift_down(self, mod):
        if mod & pygame.KMOD_LSHIFT or mod & pygame.KMOD_RSHIFT:
            return True
        return False

    def check_if_shift_released(self, key):
        lshift = pygame.K_LSHIFT
        rshift = pygame.K_RSHIFT
        if key == lshift or key == rshift:
            return None
        return False
    
    def check_lower_keys(self, key):
        if key == self.get_key(0):
            return True
        return False
