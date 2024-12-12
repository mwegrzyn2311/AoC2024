from utils.file_loader import load
from utils.common import Map2, Vector2, NEIGH_DIRS


def main():
    solution(load('12.txt'))


def solution(lines: list[str]):
    fields: Map2 = Map2(lines)
    print(total_cost(fields))

def total_cost(fields: Map2):
    visited: set[Vector2] = set()
    res: int = 0
    for y in range(len(fields.items)):
        for x in range(len(fields.items[0])):
            pos = Vector2(x, y)
            if pos not in visited:
                area: int = len(visited)
                perimeter: int = current_field_cost(fields, visited, fields[pos], pos)
                area = len(visited) - area
                res += perimeter * area
    return res

def current_field_cost(fields: Map2, visited: set[Vector2], symbol: str, curr_pos: Vector2) -> int:
    if not fields.is_in_map(curr_pos):
        return 1
    curr_symbol: str = fields[curr_pos]
    if symbol != curr_symbol:
        return 1
    if curr_pos in visited:
        return 0
    visited.add(curr_pos)
    return sum([current_field_cost(fields, visited, symbol, curr_pos + neigh_dir) for neigh_dir in NEIGH_DIRS])

main()