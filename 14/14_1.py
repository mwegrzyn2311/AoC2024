from utils.file_loader import load
from utils.common import Vector2, UP_LEFT, DOWN_LEFT, UP_RIGHT, DOWN_RIGHT

HEIGHT: int = 103
WIDTH: int = 101
TIME_LIMIT = 100

class Robot:
    initial_pos: Vector2
    vel: Vector2
    accessible_positions: list[Vector2]

    def __init__(self, pos: Vector2, vel: Vector2):
        self.initial_pos = pos
        self.vel = vel
        self.calculate_accessible_positions()

    def calculate_accessible_positions(self):
        self.accessible_positions = [self.initial_pos]
        curr_pos: Vector2 = self.initial_pos
        for i in range(TIME_LIMIT):
            curr_pos = (curr_pos + self.vel)
            curr_pos.x = curr_pos.x % WIDTH
            curr_pos.y = curr_pos.y % HEIGHT
            if curr_pos in self.accessible_positions:
                return
            else:
                self.accessible_positions.append(curr_pos)

    def get_pos_at_timestamp(self, timestamp: int) -> Vector2:
        return self.accessible_positions[timestamp % len(self.accessible_positions)]

def main():
    solution(load('14.txt'))

def solution(lines: list[str]):
    robots: list[Robot] = []
    for line in lines:
        vectors: list[str] = line.split()
        robots.append(Robot(str_to_vec(vectors[0]), str_to_vec(vectors[1])))
    quarters: dict[Vector2, int] = {UP_LEFT: 0, UP_RIGHT: 0, DOWN_RIGHT: 0, DOWN_LEFT: 0}
    middle_horiz: int = (WIDTH - 1) // 2
    middle_vert: int = (HEIGHT - 1 ) // 2
    for robot in robots:
        robot_pos: Vector2 = robot.get_pos_at_timestamp(TIME_LIMIT)
        if robot_pos.x != middle_horiz and robot_pos.y != middle_vert:
            quarters[Vector2(-1 if robot_pos.x < middle_horiz else 1, -1 if robot_pos.y < middle_vert else 1)] += 1
    score: int = quarters[UP_LEFT] * quarters[UP_RIGHT] * quarters[DOWN_LEFT] * quarters[DOWN_RIGHT]

    print(score)


def str_to_vec(half_line: str) -> Vector2:
    x_y: list[str] = half_line.strip("p=").strip("v=").split(",")
    return Vector2(int(x_y[0]), int(x_y[1]))

main()