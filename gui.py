import pygame
pygame.init()


class gui():
    def __init__(self, game):
        self.disp = pygame.display.set_mode((450, 450))
        self.board = self.boardinit()
        self.game = game

    def boardinit(self):
        background = pygame.Surface(self.disp.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        return background

    def updateBoard(self):
        self.drawBoard()
        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()

    def drawBoard(self):
        # draw buttons for different modes and highscores
        font = pygame.font.Font(None, 30)
        self.board.fill((250, 250, 250))
        chars = [chr(i) for i in self.game.getKeys()]

        text = font.render(f"{' '.join(chars)}", 1, (0, 0, 0))
        self.board.blit(text, (10, 200))

    def drawStatus(self, char, height, width):
        font = pygame.font.Font(None, 30)
        self.board.fill((250, 250, 250))
        text = font.render(f"{char}", 10, (0, 0, 0))
        self.board.blit(text, (height, width))
        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()

    def drawEndScreen(self):

        points = self.game.getPoints()
        self.drawStatus(f"RIP! You got {points} Points", 100, 100)
        pygame.time.wait(1000)

