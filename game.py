from keygenerator import keygenerator
from gui import gui
import pygame
from pygame.locals import *
pygame.init()


class game(keygenerator):

    def __init__(self):
        keygenerator.__init__(self)
        self.gameover = False
        self.points = 0
        self.gui = None
        self.clock = pygame.time.Clock()
        self.first = True
        self.total_time = 0

    def remove_key(self):
        self.remove_first_key()

    def check_keys(self, key, mod):
        correct_key = self.check_key_test(key, mod)
        if correct_key:
            self.update_game()
        elif correct_key == None:
            pass 
        else:
            self.set_gameover(True)
    
    def update_game(self):
        self.add_one_point()
        self.remove_key()
        self.update_clock()

    def update_clock(self):
        self.check_if_first()
        self.clock.tick()
        self.total_time += self.clock.get_time()
    
    def check_if_first(self):
        if self.first:
            self.clock.tick()
            self.first = False

    def get_gameover(self):
        return self.gameover

    def set_gameover(self, gameover):
        self.gameover = gameover

    def add_one_point(self):
        self.points += 1 

    def get_points(self):
        return self.points

    def get_words_per_min(self):
        return self.calculate_words_per_min()

    def calculate_words_per_min(self):
        wpm = 0
        if self.total_time != 0:
            cps = self.points // (self.total_time / 1000)
            wpm = cps * 60 / 5
            print(wpm)
        return wpm

    def get_total_time_in_sec(self):
        return self.total_time / 1000  # convert ms to s

    def create_game(self, mode):
        self.set_mode(mode)
        self.gui = gui(self)
        self.game_loop()

    def game_loop(self):
        while not self.get_gameover():
            for event in pygame.event.get():
                if event.type is QUIT:
                    self.set_gameover(True)
                if event.type == pygame.KEYUP:
                    self.check_keys(event.key, event.mod)
            self.gui.update_board()
        self.gui.draw_end_screen()

        while True:
            for event in pygame.event.get():
                if event.type is QUIT:
                    pygame.quit()
