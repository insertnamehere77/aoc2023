import sys
from dataclasses import dataclass


def read_input_lines(file_path: str) -> [str]:
    file = open(file_path, "r")
    return list(filter(lambda line: line != "", file.read().split("\n")))


@dataclass
class Round:
    num_red: int = 0
    num_blue: int = 0
    num_green: int = 0


@dataclass
class Game:
    id: int
    rounds: [Round]

    def is_possible(
        self, max_num_red: int, max_num_blue: int, max_num_green: int
    ) -> bool:
        return all(
            round.num_red <= max_num_red
            and round.num_blue <= max_num_blue
            and round.num_green <= max_num_green
            for round in self.rounds
        )


def parse_round(round_str: str):
    pulls = round_str.split(", ")
    round = Round()
    for pull in pulls:
        num, color = pull.split(" ")
        if color == "red":
            round.num_red += int(num)
        if color == "blue":
            round.num_blue += int(num)
        if color == "green":
            round.num_green += int(num)

    return round


def parse_line_into_game(line: str) -> Game:
    raw_game_str, all_rounds_str = line.split(": ")
    game_id = int(raw_game_str[5:])
    rounds = [parse_round(round_str.strip()) for round_str in all_rounds_str.split(";")]
    return Game(game_id, rounds)


def main(file_path: str):
    lines = read_input_lines(file_path)
    total = 0
    for line in lines:
        game = parse_line_into_game(line)
        if game.is_possible(max_num_red=12, max_num_blue=14, max_num_green=13):
            total += game.id

    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
