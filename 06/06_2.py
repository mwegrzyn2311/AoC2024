from utils.file_loader import load
from utils.common import Map2, Vector2, UP

def find_guard_pos(lines) -> Vector2:
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '^':
                return Vector2(x, y)

class GuardMap(Map2):
    initial_guardian_pos: Vector2
    guard_pos: Vector2
    guard_dir: Vector2
    unique_pos: set[Vector2]

    def __init__(self, lines):
        self.initial_guardian_pos = find_guard_pos(lines)
        self.guard_pos = self.initial_guardian_pos
        self.guard_dir = UP
        self.unique_pos = set()
        super().__init__(lines)

    def count_loop_causing_obstructions(self) -> int:
        self.simulate_movement()
        self.unique_pos.remove(self.initial_guardian_pos)
        res: int = 0
        for pos in self.unique_pos:
            self[pos] = '#'
            if self.is_loop_movement():
                res += 1
            self[pos] = '.'
        return res

    def is_loop_movement(self) -> bool:
        unique_pos_dir_map: dict[Vector2, set[Vector2]] = {}
        local_guard_dir: Vector2 = UP
        local_guard_pos: Vector2 = self.initial_guardian_pos
        while self.is_in_map(local_guard_pos):
            if local_guard_dir in unique_pos_dir_map.get(local_guard_pos, set()):
                return True
            if local_guard_pos not in unique_pos_dir_map:
                unique_pos_dir_map[local_guard_pos] = {local_guard_dir}
            else:
                unique_pos_dir_map[local_guard_pos].add(local_guard_dir)
            new_pos: Vector2 = local_guard_pos + local_guard_dir
            if self[new_pos] == '#':
                local_guard_dir = local_guard_dir.turn90right_simple()
            else:
                local_guard_pos = new_pos
        return False

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
    print(GuardMap(lines).count_loop_causing_obstructions())


main()