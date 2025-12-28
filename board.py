from board_entity import Board_Entity
from typing import List, Dict

class Board:
    def __init__(self, entities: List[Board_Entity], size: int = 100):
        if size < 2:
            raise ValueError("Board size should be atleast 2")
        self.size = size
        self.snakes_and_ladders = {}
        self.load_entities(entities)

    def load_entities(self, entities: List[Board_Entity]):
        for entity in entities:
            start = entity.start
            end = entity.end

            if not 1 <= start <= self.size:
                raise ValueError("Entity start must lie between the bounds")
            if not 1 <= end <= self.size:
                raise ValueError("Entity end must lie between the bounds")
            if start in self.snakes_and_ladders:
                raise ValueError("There exists another entity with the same start")
            self.snakes_and_ladders[start] = end
    
    def get_final_position(self, position: int):
        return self.snakes_and_ladders.get(position, position)
    
    def get_size(self):
        return self.size