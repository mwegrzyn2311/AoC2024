from utils.file_loader import load
from utils.common import Map2, Vector2, UP, LEFT, RIGHT, DOWN


class Warehouse(Map2):
    robot: Vector2

    def __init__(self, items):
        super().__init__(items)
        for y in range(len(self.items)):
            for x in range(len(self.items[0])):
                if self.items[y][x] == '@':
                    self.robot = Vector2(x, y)

    def move_robot(self, move: Vector2):
        new_robot_pos: Vector2 = self.robot + move
        if self[new_robot_pos] == '.':
            self[self.robot] = '.'
            self.robot = new_robot_pos
            self[self.robot] = '@'
        elif self[new_robot_pos] == 'O':
            new_box_pos: Vector2 = new_robot_pos + move
            while self[new_box_pos] == 'O':
                new_box_pos += move
            if self[new_box_pos] == '.':
                self[self.robot] = '.'
                self.robot = new_robot_pos
                self[self.robot] = '@'
                self[new_box_pos] = 'O'

    def calc_gps(self) -> int:
        res: int = 0
        for y in range(len(self.items)):
            for x in range(len(self.items)):
                if self.items[y][x] == 'O':
                    res += (100 * y + x)
        return res


def main():
    solution(load('15.txt'))

def solution(lines: list[str]):
    i: int = 0
    while lines[i] != "\n":
        i += 1
    warehouse: Warehouse = Warehouse(lines[:i])
    moves: list[Vector2] = []
    for line in lines[i+1:]:
        moves += filter(lambda move: move != Vector2(0,0), [move_from_char(char) for char in line])

    for move in moves:
        warehouse.move_robot(move)

    print(warehouse.calc_gps())

def move_from_char(char) -> Vector2:
    return UP if char == '^' else DOWN if char == 'v' else LEFT if char == '<' else RIGHT if char == '>' else Vector2(0,0)

main()