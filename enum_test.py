from enum import Enum
from typing import Iterable

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED == Color.RED)

for color in Color:
    print("--------------------------------")
    print(color)
    print(color.value)
    print(color.name)


class Turn(Enum):
    LEFT = -2
    RIGHT = -1

class Direction(Enum):
    EAST = (1, 0)
    WEST = (-1, 0)
    NORTH = (0, 1)
    SOUTH = (0, -1)

for direction in Direction:
    print("--------------------------------")
    print(direction.name)
    a, b = direction.value
    print(a, b)
    print("--------------------------------")