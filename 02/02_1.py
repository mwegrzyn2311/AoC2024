from utils.file_loader import load


def main():
    solution(load('02.txt'))


def solution(lines: list[str]):
    res: int = sum([1 if is_report_safe(line) else 0 for line in lines])
    print(res)

def is_report_safe(line: str) -> bool:
    levels: list[int] = [int(num_str) for num_str in line.split()]
    diff1: int = levels[1] - levels[0]
    diffs : list[int] = [levels[i] - levels[i - 1] for i in range(1, len(levels))]
    for diff in diffs:
        if diff1 * diff <= 0 or abs(diff) > 3:
            return False
    return True

main()