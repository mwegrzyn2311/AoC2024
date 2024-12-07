import re
from utils.file_loader import load

mul_pattern = re.compile("mul\((?P<a>\d+),(?P<b>\d+)\)")
do_pattern = re.compile("do\(\)")
dont_pattern = re.compile("don't\(\)")

def main():
    solution(load('03.txt'))


def solution(lines: list[str]):
    print(sum([count_muls(line) for line in lines]))
# 91634027
def count_muls(line: str) -> int:
    left: int = 0
    right: int = 0
    res: int = 0
    while right < len(line):
        dont_match: re.Match = re.search(dont_pattern, line[left:])
        right = len(line) if dont_match is None else left + dont_match.span()[0]
        matches: list[tuple[str, str]] = re.findall(mul_pattern, line[left:right])
        res += sum([int(match[0]) * int(match[1]) for match in matches])

        do_match: re.Match = re.search(do_pattern, line[right:])
        if do_match is None:
            return res
        else:
            left = right + do_match.span()[1]

    return res

main()