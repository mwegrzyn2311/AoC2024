from utils.file_loader import load
from utils.common import Map2, Vector2, NEIGH_DIRS


def main():
    solution(load('10.txt'))


def solution(lines: list[str]):
    mountain = Map2(lines)
    res: int = sum([trailhead_score(Vector2(x, y), mountain) for y in range(len(lines)) for x in range(len(lines[0]))])
    print(res)

def trailhead_score(initial_pos: Vector2, mountain: Map2) -> int:
    if mountain[initial_pos] != '0':
        return 0
    res = trailhead_score_rec(initial_pos, mountain, -1)
    return res

def trailhead_score_rec(pos: Vector2, mountain: Map2, last_val: int) -> int:
    curr_val_str = mountain[pos]
    if curr_val_str is None:
        return 0
    curr_val: int = int(curr_val_str)
    if curr_val != last_val + 1:
        return 0
    elif curr_val == 9:
        return 1
    else:
        return sum([trailhead_score_rec(pos + neigh_dir, mountain, curr_val) for neigh_dir in NEIGH_DIRS])

main()