from dataclasses import dataclass
from math import sqrt


@dataclass(slots=True, repr=False)
class Vector:
    x: int
    y: int

    @property
    def distance(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def pos(self):
        return [self.x, self.y]

    def direction(self, other):
        length = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return Vector((self.x - other.x) / length, (self.y - other.y) / length)

    def __sub__(self, other):
        match other:
            case Vector(x, y):
                return Vector(self.x - x, self.y - y)
            case _:
                raise Exception(
                    f"Second argument needs to be an Vector object you send {type(other)}"
                )
