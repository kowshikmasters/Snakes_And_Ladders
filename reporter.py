from abc import ABC, abstractmethod
from typing import Iterable, Dict

class Reporter(ABC):
    @abstractmethod
    def game_started(self, players: Iterable[str], board_size: int) -> None:
        pass

    @abstractmethod
    def turn_started(self, player_name: str, roll: int) -> None:
        pass

    @abstractmethod
    def invalid_move(self, player_name: str, target: int, board_size: int) -> None:
        pass

    @abstractmethod
    def ladder(self, player_name: str, start: int, end: int) -> None:
        pass

    @abstractmethod
    def snake(self, player_name: str, start: int, end: int) -> None:
        pass

    @abstractmethod
    def moved(self, player_name: str, start: int, end: int) -> None:
        pass

    @abstractmethod
    def positions(self, positions: Dict[str, int]) -> None:
        pass

    @abstractmethod
    def extra_turn(self, player_name: str) -> None:
        pass

    @abstractmethod
    def game_finished(self, winner_name: str) -> None:
        pass

#Reporter only contains stateless print methods, so it doesnt need a constructor.

class Console_Reporter(Reporter):
    def game_started(self, players: Iterable[str], board_size: int) -> None:
        print(f"Game started on a {board_size}-cell board with players: {', '.join(players)}.")

    def turn_started(self, player_name: str, roll: int) -> None:
        print(f"\n{player_name}'s turn. Rolled a {roll}.")

    def invalid_move(self, player_name: str, target: int, board_size: int) -> None:
        print(f"{player_name} needs to land exactly on {board_size}. Move to {target} is ignored.")

    def ladder(self, player_name: str, start: int, end: int) -> None:
        print(f"{player_name} found a ladder at {start} and climbed to {end}.")

    def snake(self, player_name: str, start: int, end: int) -> None:
        print(f"{player_name} was bitten by a snake at {start} and slid to {end}.")

    def moved(self, player_name: str, start: int, end: int) -> None:
        print(f"{player_name} moved from {start} to {end}.")

    def positions(self, positions: Dict[str, int]) -> None:
        parts = [f"{name}: {pos}" for name, pos in positions.items()]
        print("Positions: " + ", ".join(parts))

    def extra_turn(self, player_name: str) -> None:
        print(f"{player_name} rolled a 6 and gets another turn.")

    def game_finished(self, winner_name: str) -> None:
        print(f"Game finished! Winner: {winner_name}.")
