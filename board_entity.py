from abc import ABC, abstractmethod

class Board_Entity(ABC):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.validate()
    
    @abstractmethod
    def validate(self):
        pass

    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end