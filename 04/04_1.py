from utils.file_loader import load
from utils.common import Map2, Vector2, NEIGH_8_DIRS

next_letter: dict[str, str] = {
    'X' : 'M',
    'M' : 'A',
    'A' : 'S'
}

def main():
    solution(load('04.txt'))

def solution(lines: list[str]):
    print(count_xmas_total(lines))

def count_xmas_total(lines: list[str]) -> int:
    letters: Map2 = Map2(lines)
    all_vectors: list[Vector2] = [Vector2(x, y) for x in range(len(lines[0])) for y in range(len(lines))]
    return sum([count_xmas_from_pos(letters, curr_pos) for curr_pos in all_vectors])

def count_xmas_from_pos(letters: Map2, curr_pos: Vector2, curr_letter: str = 'X', curr_dir: Vector2 = None) -> int:
    if letters[curr_pos] != curr_letter:
        return 0
    if letters[curr_pos] == 'S':
        return 1
    if curr_dir is None:
        return sum([count_xmas_from_pos(letters, curr_pos + next_dir, next_letter[curr_letter], next_dir) for next_dir in NEIGH_8_DIRS])
    else:
        return count_xmas_from_pos(letters, curr_pos + curr_dir, next_letter[curr_letter], curr_dir)

main()