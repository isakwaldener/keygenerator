from keygenerator import keygenerator
from gui import gui
from Modes import Modes
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
        correct_key = self.check_if_correct_key(key, mod)
        if correct_key:
            self.update_game()
        elif correct_key is not None: 
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
        one_min_in_seconds = 60
        chars_per_word = 5
        if self.total_time != 0:
            cps = self.points // self.get_total_time_in_sec() 
            wpm = cps * one_min_in_seconds / chars_per_word
        return wpm

    def get_total_time_in_sec(self):
        return self.total_time / 1000  

    def create_game(self, mode):
        self.set_mode(mode)
        self.gui = gui(self)
        self.game_loop()

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if not self.get_gameover():
                    if event.type is QUIT:
                        running = False
                    if event.type == pygame.KEYUP:
                        self.check_keys(event.key, event.mod)
                    self.gui.update_board()
                else:
                    if event.type is QUIT:
                        running = False
                    if event.type == pygame.KEYUP:
                        if event.key == ord('1'):
                            self.restart(Modes.lower)
                        if event.key == ord('2'):
                            self.restart(Modes.upper)
                        if event.key == ord('3'):
                            self.restart(Modes.abc)
                        if event.key == 27:
                            running = False
            if self.get_gameover():
                self.gui.draw_end_screen()


    def restart(self, mode):
        # restart clock
        self.set_gameover(False)
        self.set_mode(mode)
        self.generate_new_keys()
        self.total_time = 0
        self.points = 0
        self.first = True
        self.gui.update_board()


