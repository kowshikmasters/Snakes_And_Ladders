from board_entity import Board_Entity

class Snake(Board_Entity):
    def validate(self):
        if self.start <= self.end:
            raise ValueError("Snake head must be at a higher position than its tail.")