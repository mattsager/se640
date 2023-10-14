from character import Character
import random


class GameGrid:
    def __init__(self) -> None:
        random.seed()
        self.grid_size = (5,5)
        self.grid_locs = [[row, col] for row in range(5) for col in range(5)]
        #initialize golden carrot location
        self.golden_carrot1 = {'sprite': '(C)', 'x':0, 'y':0, 'character':'' }
        self.golden_carrot2 = {'sprite': '(C)', 'x':0, 'y':0, 'character':'' }
        #initialize mountain location
        self.mountain = {'sprite': '(F)', 'x':0, 'y':0}
        self.character_list = []
        self.turn_cycle_counter = 0


    def add_character(self, looney_character):
        self.character_list.append(looney_character)

    def remove_character(self, looney_character ):
        self.character_list.remove(looney_character)

    def restart(self):
        pass

    def is_valid_move(grid_loc):
        # check:
        # -the loc of all pieces to verfiy that none are overlapping (except for marvin)
        # -if the move is on top of a carrot or mountain
        # -if the move is outside of the grid
        pass

    def next_turn(self):
        pass

    def get_random_move():
        valid_moves = ['up', 'down', 'left', 'right']
        move = {'x':0, 'y':0}
        direction = random.choice(valid_moves)

        if direction == 'up':
            move['y'] = 1
        elif direction == 'down':
            move['y'] = -1
        elif direction == 'right':
            move['x'] = 1
        else:
            move['x'] = -1

        return move

    def get_random_loc(self):
        available_locs = self.grid_locs
        available_locs.remove[self.mountain['x'], self.mountain['y']]

        if self.golden_carrot1['character'] != '':
            available_locs.remove[self.golden_carrot1['x'], self.golden_carrot1['y']]
        
        if self.golden_carrot2['character'] != '':
            available_locs.remove[self.golden_carrot2['x'], self.golden_carrot2['y']]

        for c in self.character_list:
            available_locs.remove[c.loc['x'], c.loc['y']]

        #return {'x':random.randint(1, 5), 'y':random.randint(1, 5)}
        return {'x':random.choice(available_locs['col']), 'y':random.choice(available_locs['row'])}

    def print_game_board(self):
        pass