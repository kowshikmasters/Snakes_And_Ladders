from collections import deque
from typing import Deque, List, Optional

from board_entity import Board_Entity
from board import Board
from player import Player
from dice import Dice
from game_status import GAME_STATUS
from reporter import Reporter, Console_Reporter

class Game:
    class Builder:
        def __init__(self):
            self.board = None
            self.players = None
            self.dice = None
            self.reporter = Console_Reporter()

        def set_board(self, board_size: int, board_entities: List[Board_Entity]):
            self.board = Board(board_entities, board_size)
            return self
        
        def set_players(self, player_names: List[str]):
            if len(player_names) < 2:
                raise ValueError("Atleast 2 players are required")
            self.players = [Player(player) for player in player_names]
            return self
        
        def set_dice(self, dice: Dice):
            self.dice = dice
            return self
        
        def set_reporter(self, reporter: Reporter):
            self.reporter = reporter
            return self

        def build(self):
            if self.board is None or self.players is None or self.dice is None:
                raise ValueError("Game configuration is incomplete. Check if the Board, Players and Dice are comfigured.")
            return Game(self)
    
    def __init__(self, build: 'Game.Builder'):
        self.board = build.board
        self.players = list(build.players)
        self.turn_order: Deque[Player] = deque(build.players)
        self.dice = build.dice
        self.reporter = build.reporter
        self.status = GAME_STATUS.NOT_STARTED
        self.winner: Optional[Player] = None

    def play(self):
        self.status = GAME_STATUS.IN_PROGRESS
        self.reporter.game_started([player.get_name() for player in self.players], self.board.get_size())

        while self.status == GAME_STATUS.IN_PROGRESS:
            press_enter = input("Press the ENTER key to roll the dice")
            current_player = self.turn_order.popleft()
            self._take_turns(current_player)
            if self.status != GAME_STATUS.IN_PROGRESS:
                break
            self.turn_order.append(current_player)

    def _take_turns(self, player: Player):
        while self.status == GAME_STATUS.IN_PROGRESS:
            roll = self.dice.roll()
            self.reporter.turn_started(player.get_name(), roll)

            curr_position = player.get_position()
            next_position = curr_position + roll

            if next_position > self.board.get_size():
                self.reporter.invalid_move(player.get_name(), next_position, self.board.get_size())
            
            elif next_position == self.board.get_size():
                self.status = GAME_STATUS.GAME_OVER
                self.winner = player
                player.set_position(next_position)
                self.reporter.positions(self._get_positions())
                self.reporter.game_finished(player.get_name())
                return
            
            else:
                final_position = self.board.get_final_position(next_position)

                if final_position > next_position:
                    self.reporter.ladder(player.get_name(), next_position, final_position)
                elif final_position < next_position:
                    self.reporter.snake(player.get_name(), next_position, final_position)
                else:
                    self.reporter.moved(player.get_name(), curr_position, final_position)

                player.set_position(final_position)
                self.reporter.positions(self._get_positions())
            
            if roll != 6:
                break
            self.reporter.extra_turn(player.get_name())


    #helper methods
    def _get_positions(self):
        return {player.get_name(): player.get_position() for player in self.players}