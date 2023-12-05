import sys


def read_input_lines(file_path: str) -> [str]:
    file = open(file_path, "r")
    return list(filter(lambda line: line != "", file.read().split("\n")))


def parse_calibration_values(line: str) -> int:
    digits = list(filter(lambda char: char.isdigit(), line))
    return int(digits[0] + digits[-1])


def main(file_path: str):
    lines = read_input_lines(file_path)
    calibration_sum = 0
    for line in lines:
        calibration_sum += parse_calibration_values(line)

    print(calibration_sum)


if __name__ == "__main__":
    main(sys.argv[1])
