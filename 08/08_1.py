from utils.file_loader import load
from utils.common import Vector2, Map2


def main():
    solution(load('08.txt'))


def solution(lines: list[str]):
    city: Map2 = Map2(lines)
    antinodes: set[Vector2] = set()
    antennas: dict[str, list[Vector2]] = parse_lines(lines)
    for key, locations in antennas.items():
        for loc1 in locations:
            for loc2 in locations:
                if loc1 != loc2:
                    antinode_pos: Vector2 = calculate_antinode_pos(loc1, loc2)
                    if city.is_in_map(antinode_pos):
                        antinodes.add(antinode_pos)

    print(len(antinodes))

def parse_lines(lines: list[str]) -> dict[str, list[Vector2]]:
    res: dict[str, list[Vector2]] = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            curr_char: str = lines[y][x]
            if curr_char != '.':
                res[curr_char] = res.get(curr_char, []) + [Vector2(x, y)]
    return res

def calculate_antinode_pos(loc1: Vector2, loc2: Vector2) -> Vector2:
    return loc1 + (loc1 - loc2)

main()