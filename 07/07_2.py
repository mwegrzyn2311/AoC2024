from utils.file_loader import load


def main():
    solution(load('07.txt'))


def solution(lines: list[str]):
    res: int = sum([score_if_calc_possible(line) for line in lines])
    print(res)

def score_if_calc_possible(line: str) -> int:
    score_and_numbers = line.split(':')
    score = int(score_and_numbers[0])
    numbers = [int(num_str) for num_str in score_and_numbers[1].split()]
    return score if is_calc_possible(score, numbers[0], numbers, 1) else 0

def is_calc_possible(target_score: int, curr_score: int, numbers: list[int], index: int) -> bool:
    if index == len(numbers):
        return curr_score == target_score
    if curr_score > target_score:
        return False
    next_num: int = numbers[index]
    return (is_calc_possible(target_score, curr_score * next_num, numbers, index + 1)
            or is_calc_possible(target_score, curr_score + next_num, numbers, index + 1)
            or is_calc_possible(target_score, int(str(curr_score) + str(next_num)), numbers, index + 1))

main()