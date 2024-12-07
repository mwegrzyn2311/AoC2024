class Vector2:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def is_in_map(self, width: int, height: int) -> bool:
        return 0 <= self.x < width and 0 <= self.y < height

    def is_vertical(self) -> bool:
        return self.x == 0

    def is_horizontal(self) -> bool:
        return self.y == 0

    def normal_vectors(self):
        if self.x == 0:
            return [Vector2(-1, 0), Vector2(1, 0)]
        elif self.y == 0:
            return [Vector2(0, -1), Vector2(0, 1)]
        else:
            return []

    def is_opposite_vector(self, other) -> bool:
        return self.x == -other.x and self.y == -other.y

    def is_parallel(self, other) -> bool:
        return (self.x == 0 and other.x == 0) or (self.y == 0 and other.y == 0)

    def turn90right_simple(self):
        if self == UP:
            return RIGHT
        elif self == RIGHT:
            return DOWN
        elif self == DOWN:
            return LEFT
        elif self == LEFT:
            return UP
        else:
            return None

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return self.x * 3 + self.y * 7

    def __lt__(self, other):
        return self.y < other.y or (self.y == other.y and self.x < other.x)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()


UP: Vector2 = Vector2(0, -1)
DOWN: Vector2 = Vector2(0, 1)
LEFT: Vector2 = Vector2(-1, 0)
RIGHT: Vector2 = Vector2(1, 0)
UP_RIGHT: Vector2 = UP + RIGHT
DOWN_RIGHT: Vector2 = DOWN + RIGHT
DOWN_LEFT: Vector2 = DOWN + LEFT
UP_LEFT: Vector2 = UP + LEFT
NEIGH_DIRS: list[Vector2] = [UP, DOWN, LEFT, RIGHT]
NEIGH_8_DIRS: list[Vector2] = [UP, UP_RIGHT, RIGHT, DOWN_RIGHT, DOWN, DOWN_LEFT, LEFT, UP_LEFT]

def vec_from_str(vec_str: str) -> Vector2:
    if vec_str in ('U', 'UP'):
        return UP
    elif vec_str in ('D', 'DOWN'):
        return DOWN
    elif vec_str in ('L', 'LEFT'):
        return LEFT
    elif vec_str in ('R', 'RIGHT'):
        return RIGHT
    else:
        return Vector2(0, 0)


class Vector3:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def get_surf(self) -> Vector2:
        return Vector2(self.x, self.y)

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return self.x * 3 + self.y * 7 + self.z * 11

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

class Map2:
    def __init__(self, items):
        self.items = [item.strip('\n') for item in items]

    def __getitem__(self, vec2: Vector2):
        return self.items[vec2.y][vec2.x] if self.is_in_map(vec2) else None

    def __setitem__(self, vec2: Vector2, new_val):
        if self.is_in_map(vec2):
            self.items[vec2.y] = self.items[vec2.y][:vec2.x] + new_val + self.items[vec2.y][vec2.x + 1:]

    def is_in_map(self, vec2: Vector2) -> bool:
        return 0 <= vec2.x < len(self.items[0]) and 0 <= vec2.y < len(self.items)

UNIT_3_X = Vector3(1, 0, 0)
UNIT_3_Y = Vector3(0, 1, 0)
UNIT_3_Z = Vector3(0, 0, 1)
VEC_3_ONE = Vector3(1, 1, 1)