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
        xscore += 10000000000000
        yscore += 10000000000000
        res += calc_button_pushes(xa, ya, xb, yb, xscore, yscore)
        i += 4
    print(res)

def calc_button_pushes(xa: int, ya: int, xb: int, yb: int, xscore: int, yscore: int) -> int:
    b = xscore / (xb - yb * (xa / ya)) - (yscore / (xb * ya / xa - yb))
    if b > 0 and my_is_integer(b):
        b = round(b)
    else:
        return 0
    a = (xscore - xb * b) / xa
    return round(a) * 3 + b if (a > 0 and my_is_integer(a)) else 0

def my_is_integer(num: float) -> bool:
    return abs(num - round(num)) <= 0.0001

def parse_line(line: str) -> tuple[int, int]:
    button_a: list[str] = line.split(': ')[1].split(', ')
    return int(button_a[0].strip('X+').strip('X=')), int(button_a[1].strip('Y+').strip('Y='))

main()