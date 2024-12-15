from utils.file_loader import load
from utils.common import Vector2
from PIL import Image

HEIGHT: int = 103
WIDTH: int = 101

GREEN: tuple[int, int, int] = (0, 255, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)

TIME_LIMIT: int = 10000

class Robot:
    initial_pos: Vector2
    vel: Vector2
    curr_pos: Vector2

    def __init__(self, pos: Vector2, vel: Vector2):
        self.initial_pos = pos
        self.vel = vel
        self.curr_pos = self.initial_pos

    def move(self):
        self.curr_pos = self.curr_pos + self.vel
        self.curr_pos.x = self.curr_pos.x % WIDTH
        self.curr_pos.y = self.curr_pos.y % HEIGHT

def main():
    solution(load('14.txt'))

def solution(lines: list[str]):
    robots: list[Robot] = []
    for line in lines:
        vectors: list[str] = line.split()
        robots.append(Robot(str_to_vec(vectors[0]), str_to_vec(vectors[1])))

    for i in range(TIME_LIMIT):
        robot_positions: set[Vector2] = set()
        for robot in robots:
            robot.move()
            robot_positions.add(robot.curr_pos)
        if i + 1 == 6377:
            display_curr_state(robot_positions, i + 1)

def display_curr_state(robot_positions: set[Vector2], timestamp: int):
    img = Image.new('RGB', (WIDTH, HEIGHT))
    img.putdata([GREEN if Vector2(x, y) in robot_positions else WHITE for y in range(HEIGHT) for x in range(WIDTH)])
    img.save(f'output/14_2_res/{str(timestamp).zfill(5)}.png')
# 115, 216 sus

def str_to_vec(half_line: str) -> Vector2:
    x_y: list[str] = half_line.strip("p=").strip("v=").split(",")
    return Vector2(int(x_y[0]), int(x_y[1]))

main()