import pygame
from game_grid import GameGrid
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
        self.running = False

    def start_game(self):
        self.running = True
        self.grid = GameGrid()
        self.grid.add_character(self.bugs)
        self.grid.add_character(self.taz)
        self.grid.add_character(self.tweety)
        self.grid.add_character(self.marvin)

        #set random start locations
        self.grid.set_carrot1_loc(self.grid.get_random_loc())
        self.grid.set_carrot2_loc(self.grid.get_random_loc())
        self.grid.set_mountain_loc(self.grid.get_random_loc())

        for c in self.grid.character_list:
            loc = self.grid.get_random_loc()
            c.character_type.set_loc(loc['x'], loc['y'])

        while self.running:
            self.clock.tick(60)
            self.grid.print_game_board()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False