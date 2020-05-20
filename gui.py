from game import game
import pygame
from pygame.locals import *
pygame.init()


class gui():
    def __init__(self):
        self.disp = pygame.display.set_mode((450, 450))
        self.board = self.boardinit()
        self.game = game()

    def boardinit(self):
        background = pygame.Surface(self.disp.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        return background

    def updateBoard(self):
        self.drawBoard()
        # self.drawStatus()
        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()

    def drawBoard(self):
        # draw buttons for different modes and highscores
        font = pygame.font.Font(None, 30)
        self.board.fill((250, 250, 250))
        # char = pygame.key.name(self.game.getKey(0))
        chars = [chr(i) for i in self.game.keygenerator.getKeys()]

        text = font.render(f"{' '.join(chars)}", 1, (0, 0, 0))
        self.board.blit(text, (10, 200))

    def drawStatus(self, char, height, width):
        font = pygame.font.Font(None, 100)
        self.board.fill((250, 250, 250))
        text = font.render(f"{char}", 14, (0, 0, 0))
        self.board.blit(text, (height, width))
        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()


gui = gui()
gui.game.setModes()
gui.game.setCurrentMode("upperCase") # got some unknown keys
count = 0
exit = False 
shift = False
while(not gui.game.getGameover()):

    for event in pygame.event.get():
        if event.type is QUIT:
            exit = True

        if event.type == pygame.KEYUP:

            if gui.game.checkKeys(event.key, event.mod):
                print("here")
                gui.game.removeKey()
                # gui.drawStatus("Correct key", 100, 225)  # doesn't work atm
                count += 1
                continue
            """elif event.key != gui.game.getKey(0):
                gui.drawStatus("RIP", 100, 100)
                pygame.time.wait(1000)
                exit = True"""

    gui.updateBoard()
