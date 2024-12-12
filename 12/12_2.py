from utils.file_loader import load
from utils.common import Map2, Vector2, NEIGH_DIRS, vec2_vert_cmp_key


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
                vert_fences: list[Vector2] = []
                horiz_fences: list[Vector2] = []
                analyze_area_and_fences(fields, visited, fields[pos], pos, vert_fences, horiz_fences, pos)
                area = len(visited) - area
                fc = fences_cost(vert_fences, horiz_fences)
                print(fc * area)
                res += fc * area
    return res


def fences_cost(vert_fences: list[Vector2], horiz_fences: list[Vector2]) -> int:
    vert_fences.sort(key=vec2_vert_cmp_key, reverse=True)
    prev_fence = Vector2(-2, -2)
    vert_res: int = 0
    for fence in vert_fences:
        if fence.y != prev_fence.y or abs(fence.x - prev_fence.x) != 2 or Vector2((fence.x + prev_fence.x) // 2, fence.y + 1) in horiz_fences:
            vert_res += 1
        prev_fence = fence

    return vert_res * 2
#845490
def analyze_area_and_fences(fields: Map2, visited: set[Vector2], symbol: str, curr_pos: Vector2, vert_fences: list[Vector2], horiz_fences: list[Vector2], prev_pos: Vector2):
    if not fields.is_in_map(curr_pos):
        (vert_fences if curr_pos.x == prev_pos.x else horiz_fences).append(Vector2(prev_pos.x + curr_pos.x, prev_pos.y + curr_pos.y))
        return
    curr_symbol: str = fields[curr_pos]
    if symbol != curr_symbol:
        (vert_fences if curr_pos.x == prev_pos.x else horiz_fences).append(Vector2(prev_pos.x + curr_pos.x, prev_pos.y + curr_pos.y))
        return
    if curr_pos in visited:
        return
    visited.add(curr_pos)
    for neigh_dir in NEIGH_DIRS:
        analyze_area_and_fences(fields, visited, symbol, curr_pos + neigh_dir, vert_fences, horiz_fences, curr_pos)


main()
