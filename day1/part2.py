import sys, re


def read_input_lines(file_path: str) -> [str]:
    file = open(file_path, "r")
    return list(filter(lambda line: line != "", file.read().split("\n")))


def translate_text_to_digit(number: str) -> str:
    if number.isdigit():
        return number

    lookup = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return lookup[number]


def parse_calibration_values(line: str) -> int:
    # Had to use a weird lookahead regex trick since the numbers can overlap
    str_digits = re.findall(
        "(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
    )
    num_digits = list(map(lambda number: translate_text_to_digit(number), str_digits))
    print(num_digits[0] + num_digits[-1])
    return int(num_digits[0] + num_digits[-1])


def main(file_path: str):
    lines = read_input_lines(file_path)
    calibration_sum = 0
    for line in lines:
        calibration_sum += parse_calibration_values(line)

    print(calibration_sum)


if __name__ == "__main__":
    main(sys.argv[1])
