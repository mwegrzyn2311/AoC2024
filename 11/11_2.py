from utils.file_loader import load


def main():
    solution(load('11.txt'))


def solution(lines: list[str]):
    stones: dict[str, int] = {stone : 1 for stone in lines[0].strip("\n").split()}
    for i in range(75):
        stones = stone_cycle(stones)
    print(sum(stones.values()))

def stone_cycle(stones: dict[str, int]) -> dict[str, int]:
    new_stones: dict[str, int] = {}
    for stone, count in stones.items():
        if stone == '0':
            new_stones['1'] = new_stones.get('1', 0) + count
        elif len(stone) % 2 == 0:
            middle: int = len(stone) // 2
            left_stone = stone[:middle]
            new_stones[left_stone] = new_stones.get(left_stone, 0) + count
            right_stone = str(int(stone[middle:]))
            new_stones[right_stone] = new_stones.get(right_stone, 0) + count
        else:
            new_stone: str = str(2024 * int(stone))
            new_stones[new_stone] = new_stones.get(new_stone, 0) + count
    return new_stones

main()