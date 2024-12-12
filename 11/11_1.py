from utils.file_loader import load


def main():
    solution(load('11.txt'))


def solution(lines: list[str]):
    stones: list[str] = lines[0].strip("\n").split()
    for i in range(25):
        stones = stone_cycle(stones)
    print(len(stones))

def stone_cycle(stones: list[str]) -> list[str]:
    new_stones: list[str] = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            middle: int = len(stone) // 2
            new_stones.append(stone[:middle])
            new_stones.append(str(int(stone[middle:])))
        else:
            new_stones.append(str(2024 * int(stone)))
    return new_stones

main()