from enum import unique

from utils.file_loader import load
from utils.common import Map2, Vector2, UP

def find_guard_pos(lines) -> Vector2:
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '^':
                return Vector2(x, y)

class GuardMap(Map2):
    guard_pos: Vector2
    guard_dir: Vector2
    unique_pos: set[Vector2]

    def __init__(self, lines):
        self.guard_pos = find_guard_pos(lines)
        self.guard_dir = UP
        self.unique_pos = set()
        super().__init__(lines)

    # For now assuming that the guard will eventually leave and not loop themselves
    def simulate_movement(self):
        while self.is_in_map(self.guard_pos):
            self.unique_pos.add(self.guard_pos)
            new_pos: Vector2 = self.guard_pos + self.guard_dir
            if self[new_pos] == '#':
                self.guard_dir = self.guard_dir.turn90right_simple()
            else:
                self.guard_pos = new_pos

    def count_unique_pos(self) -> int:
        return len(self.unique_pos)

def main():
    solution(load('06.txt'))

def solution(lines: list[str]):
    guard_map: GuardMap = GuardMap(lines)
    guard_map.simulate_movement()
    print(guard_map.count_unique_pos())


main()