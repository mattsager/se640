from character import Character
import random


class GameGrid:
    def __init__(self) -> None:
        random.seed()
        grid_size = (5,5)
        grid_locs = [[row, col] for row in range(5) for col in range(5)]
        #initialize golden carrot location
        golden_carrot1 = {'x':0, 'y':0, 'character':'' }
        golden_carrot2 = {'x':0, 'y':0, 'character':'' }
        #initialize mountain location
        mountain = {'x':0, 'y':0}
        character_list = []
        turn_cycle_counter = 0


    def add_character(looney_character):
        pass

    def remove_character(looney_character ):
        pass

    def restart():
        pass

    def is_valid_move(grid_loc):
        # check the loc of all pieces to verfiy that none are overlapping (except for marvin)
        #also check if the move is on top of a carrot or mountain
        pass

    def next_turn():
        pass

    def random_movement():
        next_grid_loc = {'x':random.randint(1, 5), 'y':random.randint(1, 5)}
        GameGrid.is_valid_move(next_grid_loc)

    def print_game_board():
        pass