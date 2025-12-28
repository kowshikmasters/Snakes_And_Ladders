from board_entity import Board_Entity

class Ladder(Board_Entity):
    def validate(self):
        if self.start >= self.end:
            raise ValueError("Ladder bottom must be at a lower position than its top.")