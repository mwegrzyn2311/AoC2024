from utils.file_loader import load
from utils.common import Map2, Vector2, DOWN_LEFT, DOWN_RIGHT, UP_LEFT, UP_RIGHT

def main():
    solution(load('04.txt'))

def solution(lines: list[str]):
    print(count_xmas_total_part2(lines))

def count_xmas_total_part2(lines: list[str]) -> int:
    letters: Map2 = Map2(lines)
    potential_a_vectors: list[Vector2] = [Vector2(x, y) for x in range(1, len(lines[0]) - 1) for y in range(1, len(lines) -1)]
    return sum([count_xmas_pos_part2(letters, curr_pos) for curr_pos in potential_a_vectors])

def count_xmas_pos_part2(letters: Map2, curr_pos: Vector2) -> int:
    if letters[curr_pos] != 'A':
        return 0
    return (((letters[curr_pos + UP_RIGHT] == 'M' and letters[curr_pos + DOWN_LEFT] == 'S')
             or (letters[curr_pos + UP_RIGHT] == 'S' and letters[curr_pos + DOWN_LEFT] == 'M'))
            and ((letters[curr_pos + UP_LEFT] == 'M' and letters[curr_pos + DOWN_RIGHT] == 'S')
                 or (letters[curr_pos + UP_LEFT] == 'S' and letters[curr_pos + DOWN_RIGHT] == 'M')))



main()