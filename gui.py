import pygame
pygame.init()


class gui():
    def __init__(self, game):
        self.disp = pygame.display.set_mode((450, 450))
        self.board = self.board_init()
        self.game = game

    def board_init(self):
        background = pygame.Surface(self.disp.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
        return background

    def update_board(self):
        self.add_keys_to_board()
        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()

    def add_keys_to_board(self):
        self.draw_black_background()
        chars = self.get_chars_from_keys() 
        self.draw_keys_to_board(chars)

    def get_chars_from_keys(self):
        return [chr(i) for i in self.game.get_keys()]

    def draw_keys_to_board(self, chars):
        font = pygame.font.Font(None, 30)
        text = font.render(f"{' '.join(chars)}", 1, (0, 0, 0))
        self.board.blit(text, (10, 200))

    def draw_screen(self, end=True):
        font = pygame.font.Font(None, 30)
        self.draw_black_background()
        if end:
            self.add_points_to_endscreen(font)
        else:
            self.add_text_to_finished_screen(font)
        self.add_time_to_screen(font)
        self.add_wpm_to_screen(font)
        self.add_highscore_to_screen(font)
        self.add_lower_mode_to_screen(font)
        self.add_upper_mode_to_screen(font)
        self.add_abc_mode_to_screen(font)

        self.disp.blit(self.board, (0, 0))
        pygame.display.flip()

    def add_text_to_finished_screen(self, font):
        textPoint = font.render(f"You hit all the keys", 10, (0, 0, 0))
        self.board.blit(textPoint, (100, 100))

    def add_points_to_endscreen(self, font):
        points = self.game.get_points()
        textPoint = font.render(f"RIP! You got {points} Points", 10, (0, 0, 0))
        self.board.blit(textPoint, (100, 100))

    def add_highscore_to_screen(self, font): 
        highscore = self.game.highscore
        text_highscore = font.render(f"Best WPM: {highscore}", 10, (0, 0, 0))
        self.board.blit(text_highscore, (100, 250))
        
    def add_time_to_screen(self, font):
        time = self.game.get_total_time_in_sec()
        textTime = font.render(f"Total game time: {time}", 10, (0, 0, 0))
        self.board.blit(textTime, (100, 150))

    def add_wpm_to_screen(self, font):
        wpm = self.game.get_words_per_min()
        textWPM = font.render(f"Words per minute: {wpm}", 10, (0, 0, 0))
        self.board.blit(textWPM, (100, 200))

    def add_lower_mode_to_screen(self, font):
        wpm = self.game.get_words_per_min()
        textWPM = font.render(f"Restart with lower mode: 1", 10, (0, 0, 0))
        self.board.blit(textWPM, (100, 300))
        
    def add_upper_mode_to_screen(self, font):
        wpm = self.game.get_words_per_min()
        textWPM = font.render(f"Restart with upper mode: 2", 10, (0, 0, 0))
        self.board.blit(textWPM, (100, 350))

    def add_abc_mode_to_screen(self, font):
        wpm = self.game.get_words_per_min()
        textWPM = font.render(f"Restart with abc  mode: 3", 10, (0, 0, 0))
        self.board.blit(textWPM, (100, 400))

    def draw_black_background(self):
        self.board.fill((250, 250, 250))
