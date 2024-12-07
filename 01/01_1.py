from utils.file_loader import load


def main():
    solution(load('01.txt'))


def solution(lines: list[str]):
    # Parse lines to left and right list
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        left_and_right: list[str] = line.split()
        left.append(int(left_and_right[0]))
        right.append(int(left_and_right[1]))
    # Actual solution
    left.sort()
    right.sort()
    res: int = sum([abs(left[i] - right[i]) for i in range(len(left))])
    print(res)

main()