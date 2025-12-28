from reporter import Reporter, Console_Reporter
from board_entity import Board_Entity
from dice import Dice, Dice_Random
from player import Player
from typing import List
from game import Game

class Snakes_And_Ladder:
    def __init__(self, reporter: Reporter | None = None):
        self.reporter = reporter or Console_Reporter()

    def create_game(self, size: int, entities: List[Board_Entity], players: List[str], dice: Dice | None = None):
        chosen_dice = dice or Dice_Random(1, 6)
        return (Game.Builder()
        .set_board(size, entities)
        .set_players(players)
        .set_dice(chosen_dice)
        .set_reporter(self.reporter)
        .build())
    
    def play_game(self, size: int, entities: List[Board_Entity], players: List[str], dice: Dice | None = None):
        game = self.create_game(size, entities, players, dice)
        game.play()