from utils.file_loader import load


def main():
    solution(load('01.txt'))


def solution(lines: list[str]):
    # Parse lines to left and right list
    left: list[int] = []
    right: dict[int, int] = {}
    for line in lines:
        left_and_right: list[str] = line.split()
        left.append(int(left_and_right[0]))
        right_ele: int = int(left_and_right[1])
        right[right_ele] = right.get(right_ele, 0) + 1
    # Actual solution
    res: int = sum([left[i] * right.get(left[i], 0) for i in range(len(left))])
    print(res)

main()