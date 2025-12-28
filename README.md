# Snakes and Ladders (Python)

A simple, console-based Snakes and Ladders game built for practice. It uses a clean, beginner-friendly object-oriented design with a facade entry point.

## Features
- 100-cell board (configurable)
- Snakes and ladders with flexible start/end positions
- Round-robin turns for 2+ players
- Dice rolls (1-6) with extra turn on a 6
- Exact landing required to win
- Console output each turn
- Local play prompt for player names

## How to run
From the project root:

```bash
python Snakes_and_Ladders/local_play.py
```

## Local play
`local_play.py` asks for player names, uses a fixed set of snakes/ladders, and starts the game.

## Project structure
- `Snakes_and_Ladders/game.py`: game loop and rules
- `Snakes_and_Ladders/board.py`: board state and entity mapping
- `Snakes_and_Ladders/board_entity.py`: base class for snakes and ladders
- `Snakes_and_Ladders/snake.py`: snake entity validation
- `Snakes_and_Ladders/ladder.py`: ladder entity validation
- `Snakes_and_Ladders/dice.py`: dice abstraction + random dice
- `Snakes_and_Ladders/player.py`: player state
- `Snakes_and_Ladders/reporter.py`: console output
- `Snakes_and_Ladders/facade.py`: simple entry point for clients
- `Snakes_and_Ladders/local_play.py`: interactive local game runner

## Example usage

```python
from facade import Snakes_And_Ladder
from ladder import Ladder
from snake import Snake

board_entities = [
    Snake(17, 7), Snake(54, 34),
    Snake(62, 19), Snake(98, 79),
    Ladder(3, 38), Ladder(24, 33),
    Ladder(42, 93), Ladder(72, 84)
]

players = ["Alice", "Bob", "Charlie"]

facade = Snakes_And_Ladder()
facade.play_game(100, board_entities, players)
```

## Notes
- Multiple players can occupy the same cell.
- Output is text-only; there is no 2D board rendering.
