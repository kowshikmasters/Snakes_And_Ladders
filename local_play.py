from facade import Snakes_And_Ladder
from ladder import Ladder
from snake import Snake


def _prompt_player_names() -> list[str]:
    while True:
        raw = input("Enter player names separated by commas: ").strip()
        names = [name.strip() for name in raw.split(",") if name.strip()]
        if len(names) >= 2:
            return names
        print("Please enter at least 2 player names.")


def main() -> None:
    board_entities = [
        Snake(17, 7), Snake(54, 34),
        Snake(62, 19), Snake(98, 79),
        Ladder(3, 38), Ladder(24, 33),
        Ladder(42, 93), Ladder(72, 84),
    ]

    players = _prompt_player_names()
    facade = Snakes_And_Ladder()
    facade.play_game(100, board_entities, players)


if __name__ == "__main__":
    main()
