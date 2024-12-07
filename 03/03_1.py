import re
from utils.file_loader import load


def main():
    solution(load('03.txt'))


def solution(lines: list[str]):
    print(sum([count_muls(line) for line in lines]))

def count_muls(line: str) -> int:
    matches: list[tuple[str, str]] = re.findall("mul\((?P<a>\d+),(?P<b>\d+)\)", line)
    return sum([int(match[0]) * int(match[1]) for match in matches])

main()