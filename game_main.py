import pygame
from character import Character, BugsBunny, TazDevil, Tweety, MarvinMartian

class Main():
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.bugs = Character(BugsBunny)
        self.taz = Character(TazDevil)
        self.tweety = Character(Tweety)
        self.marvin = Character(MarvinMartian)
        self.running = True

    def start_game(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False