import pygame
from character import Character, BugsBunny, TazDevil, Tweety, MarvinMartian

class Main():
    def __init__(self) -> None:
        pygame.init()
        window = pygame.display.set_mode((1280, 720))
        
        bugs = Character(BugsBunny)
        taz = Character(TazDevil)
        tweety = Character(Tweety)
        marvin = Character(MarvinMartian)
        self.running = True

    def start_game(grid):
        while grid.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    grid.running = False