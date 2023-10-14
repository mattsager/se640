from abc import ABC, abstractmethod
from pathlib import Path

class Character:
    def __init__(self, character_type) -> None:
        self.character_type = character_type


class AbstractCharacter(ABC):
    @abstractmethod
    def get_properties(self):
        pass


class BugsBunny(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'B'
        self.loc = {'x':0, 'y':0}

    def get_properties(self):
        pass


class TazDevil(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'D'
        self.loc = {'x':0, 'y':0}

    def get_properties(self):
        return super().get_properties()


class Tweety(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'T'
        self.loc = {'x':0, 'y':0}

    def get_properties(self):
        return super().get_properties()


class MarvinMartian(AbstractCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'M'
        self.loc = {'x':0, 'y':0}

    def get_properties(self):
        return super().get_properties()