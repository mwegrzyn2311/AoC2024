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

    res: int = sum([get_middle_if_legit(line, rules) for line in lines[i + 1:]])
    print(res)

def get_middle_if_legit(line: str, rules: dict[int, list[int]]) -> int:
    numbers: list[int] = [int(num_str) for num_str in line.split('\n')[0].split(",")]
    return numbers[int((len(numbers) - 1) / 2)] if is_legit(numbers, rules) else 0

def is_legit(numbers: list[int], rules: dict[int, list[int]]) -> bool:
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] in rules:
            deps: list[int] = rules[numbers[i]]
            for j in range(0, i):
                if numbers[j] in deps:
                    return False
    return True

main()