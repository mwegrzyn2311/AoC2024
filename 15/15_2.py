from utils.file_loader import load
from utils.common import Map2, Vector2, UP, LEFT, RIGHT, DOWN

BOX = ['[', ']']

def widen(char: str) -> str:
    return '##' if char == '#' else '..' if char == '.' else '@.' if char == '@' else '[]' if char == 'O' else '!'

class Warehouse(Map2):
    robot: Vector2

    def __init__(self, items):
        super().__init__(items)

        for y in range(len(self.items)):
            new_line = ''
            for char in self.items[y]:
                new_line += widen(char)
            self.items[y] = new_line

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
        elif self[new_robot_pos] in BOX:
            if move.y == 0:
                new_box_pos: Vector2 = new_robot_pos + move
                while self[new_box_pos] in BOX:
                    new_box_pos += move
                if self[new_box_pos] == '.':
                    while new_box_pos != new_robot_pos:
                        self[new_box_pos] = self[new_box_pos - move]
                        new_box_pos = new_box_pos - move
                    self[self.robot] = '.'
                    self.robot = new_robot_pos
                    self[self.robot] = '@'

            else:
                boxes: list[list[Vector2]] = [[new_robot_pos]]
                while True:
                    curr_boxes: list[Vector2] = []
                    for box in boxes[-1]:
                        if self[box] == ']' and box + LEFT not in boxes[-1]:
                            curr_boxes.append(box + LEFT)
                        curr_boxes.append(box)
                        if self[box] == '[' and box + RIGHT not in boxes[-1]:
                            curr_boxes.append(box + RIGHT)
                    boxes[-1] = curr_boxes

                    next_line: list[Vector2] = [box + move for box in curr_boxes]

                    if self.is_rock_in_line(next_line):
                        break
                    elif self.is_box_in_line(next_line):
                        boxes_in_next: list[Vector2] = []
                        for box in curr_boxes:
                            new_pos: Vector2 = box + move
                            if self[new_pos] in BOX:
                                boxes_in_next.append(new_pos)
                        boxes.append(boxes_in_next)
                    elif self.is_empy_line(next_line):
                        boxes.reverse()
                        for box_line in boxes:
                            for box in box_line:
                                self[box + move] = self[box]
                                self[box] = '.'
                        self[self.robot] = '.'
                        self.robot = new_robot_pos
                        self[self.robot] = '@'
                        break
                    else:
                        print("WTF")

    def is_rock_in_line(self, vectors: list[Vector2]) -> bool:
        for vector in vectors:
            if self[vector] =='#':
                return True
        return False

    def is_box_in_line(self, vectors: list[Vector2]) -> bool:
        for vector in vectors:
            if self[vector] in BOX:
                return True
        return False

    def is_empy_line(self, vectors: list[Vector2]) -> bool:
        for vector in vectors:
            if self[vector] != '.':
                return False
        return True

    def calc_gps(self) -> int:
        res: int = 0
        for y in range(len(self.items)):
            for x in range(len(self.items[0])):
                if self.items[y][x] == '[':
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

    j: int = 0
    for move in moves:
        if j < 100:
            j += 1
        warehouse.move_robot(move)

    warehouse.print_map()
    print(warehouse.calc_gps())

def move_from_char(char) -> Vector2:
    return UP if char == '^' else DOWN if char == 'v' else LEFT if char == '<' else RIGHT if char == '>' else Vector2(0,0)

main()