from utils.file_loader import load
from utils.common import Vector2, Map2
from math import gcd


def main():
    solution(load('08.txt'))


def solution(lines: list[str]):
    city: Map2 = Map2(lines)
    antinodes: set[Vector2] = set()
    antennas: dict[str, list[Vector2]] = parse_lines(lines)
    for key, locations in antennas.items():
        for i in range(len(locations)):
            loc1 = locations[i]
            for loc2 in locations[i+1:]:
                    for antinode in calculate_antinode_positions(loc1, loc2, city):
                        antinodes.add(antinode)
    print(len(antinodes))

def parse_lines(lines: list[str]) -> dict[str, list[Vector2]]:
    res: dict[str, list[Vector2]] = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            curr_char: str = lines[y][x]
            if curr_char != '.':
                res[curr_char] = res.get(curr_char, []) + [Vector2(x, y)]
    return res

def calculate_antinode_positions(loc1: Vector2, loc2: Vector2, city: Map2) -> list[Vector2]:
    res: list[Vector2] = []
    offset_vec: Vector2 = loc1 - loc2
    vec_gcd: int = gcd(abs(offset_vec.x), abs(offset_vec.y))
    normalized_vec: Vector2 = offset_vec / vec_gcd
    next_pos: Vector2 = loc1
    while city.is_in_map(next_pos):
        res.append(next_pos)
        next_pos = next_pos + normalized_vec
    next_pos = loc1 - normalized_vec
    while city.is_in_map(next_pos):
        res.append(next_pos)
        next_pos = next_pos - normalized_vec
    return res

main()
