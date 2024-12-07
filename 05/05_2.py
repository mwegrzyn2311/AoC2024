from utils.file_loader import load

def main():
    solution(load('05.txt'))

def solution(lines: list[str]):
    rules: dict[int, list[int]] = {}
    i: int = 0
    while lines[i] != '\n':
        a_b: list[str] = lines[i].split('\n')[0].split("|")
        rules[int(a_b[0])] = rules.get(int(a_b[0]), []) + [int(a_b[1])]
        i += 1

    res: int = sum([get_middle_only_if_reordered(line, rules) for line in lines[i + 1:]])
    print(res)

def get_middle_only_if_reordered(line: str, rules: dict[int, list[int]]) -> int:
    numbers: list[int] = [int(num_str) for num_str in line.split('\n')[0].split(",")]
    reordered = reorder_simple(numbers, len(numbers), rules)

    return 0 if numbers == reordered else reordered[int((len(reordered) - 1) / 2)]

def reorder_simple(numbers:list[int], start_from: int, rules: dict[int, list[int]]) -> list[int]:
    for i in range(start_from - 1, -1, -1):
        if numbers[i] in rules:
            deps: list[int] = rules[numbers[i]]
            for j in range(i - 1, -1, -1):
                if numbers[j] in deps:
                    return reorder_simple(numbers[:j] + numbers[j+1:i+1] + [numbers[j]] + numbers[i+1:], i+1, rules)
    return numbers

main()