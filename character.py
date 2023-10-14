from abc import ABC, abstractmethod
from pathlib import Path

class Character:
    def __init__(self, character_type, start_loc) -> None:
        self.character_type = character_type


class AbstractCharacter(ABC):
    @abstractmethod
    def get_loc(self):
        pass

    @abstractmethod
    def set_loc(self):
        pass

    @abstractmethod
    def get_properties(self):
        pass


class BugsBunny(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'B'
        self.loc = {'x':0, 'y':0}

    def __str__(self) -> str:
        return "Bugs Bunny"

    def get_loc(self):
        return (self.loc['x'], self.loc['y'])

    def set_loc(self, x, y):
        self.loc['x'] = x
        self.loc['y'] = y
        return

    def get_properties(self):
        pass


class TazDevil(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'D'
        self.loc = {'x':0, 'y':0}

    def __str__(self) -> str:
       return "Taz"

    def get_loc(self):
        return (self.loc['x'], self.loc['y'])

    def set_loc(self, x, y):
        self.loc['x'] = x
        self.loc['y'] = y

    def get_properties(self):
        return super().get_properties()


class Tweety(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'T'
        self.loc = {'x':0, 'y':0}

    def __str__(self) -> str:
       return "Tweety"

    def get_loc(self):
        return (self.loc['x'], self.loc['y'])

    def set_loc(self, x, y):
        self.loc['x'] = x
        self.loc['y'] = y

    def get_properties(self):
        return super().get_properties()


class MarvinMartian(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'M'
        self.loc = {'x':0, 'y':0}

    def __str__(self) -> str:
       return "Marvin"

    def get_loc(self):
        return (self.loc['x'], self.loc['y'])

    def set_loc(self, x, y):
        self.loc['x'] = x
        self.loc['y'] = y

    def get_properties(self):
        return super().get_properties()