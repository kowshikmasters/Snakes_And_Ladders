from abc import ABC, abstractmethod
import random

class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass

class Dice_Random(Dice):
    def __init__(self, min_val : int, max_val: int):
        if min_val >= max_val:
            raise ValueError("The minimum value of Dice must be less the maximum value.")
        self.min_val = min_val
        self.max_val = max_val
    
    def roll(self):
        return random.randint(self.min_val, self.max_val)