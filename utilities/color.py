from dataclasses import dataclass


@dataclass
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (100, 100, 100)
    PURPLE = (148, 0, 211)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 223, 0)
