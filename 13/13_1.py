from utils.file_loader import load


def main():
    solution(load('13.txt'))


def solution(lines: list[str]):
    res: int = 0
    i: int = 0
    while i < len(lines):
        xa, ya = parse_line(lines[i])
        xb, yb = parse_line(lines[i + 1])
        xscore, yscore = parse_line(lines[i+2])
        tokens: int = calc_button_pushes(xa, ya, xb, yb, xscore, yscore)
        print(tokens)
        print("----")
        res += tokens
        i += 4
    print(res)

def calc_button_pushes(xa: int, ya: int, xb: int, yb: int, xscore: int, yscore: int) -> int:
    b = (xscore - yscore * (xa / ya)) / (xb - yb * (xa / ya))
    a = (xscore - xb * b) / xa
    print(a, b)
    return round(a) * 3 + round(b) if my_is_integer(a) and my_is_integer(b) else 0

def my_is_integer(num: float) -> bool:
    return abs(num - round(num)) <= 0.0000000001

def parse_line(line: str) -> tuple[int, int]:
    print(line)
    button_a: list[str] = line.split(': ')[1].split(', ')
    return int(button_a[0].strip('X+').strip('X=')), int(button_a[1].strip('Y+').strip('Y='))

main()