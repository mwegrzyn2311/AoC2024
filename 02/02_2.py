from utils.file_loader import load


def main():
    solution(load('02.txt'))


def solution(lines: list[str]):
    res: int = sum([1 if is_report_safe([int(num_str) for num_str in line.split()]) else 0 for line in lines])
    print(res)

def is_report_safe(levels: list[int], depth: int = 0) -> bool:
    if depth > 1:
        return False
    diff1: int = levels[1] - levels[0]
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff1 * diff <= 0 or abs(diff) > 3:
            levels_without_left: list[int] = levels.copy()
            levels_without_left.pop(i -1)
            levels_without_right: list[int] = levels.copy()
            levels_without_right.pop(i)
            levels_without_first: list[int] = levels.copy()
            levels_without_first.pop(0)
            return (is_report_safe(levels_without_left, depth + 1) or
                    is_report_safe(levels_without_right, depth + 1) or
                    is_report_safe(levels_without_first, depth + 1))
    return True

main()