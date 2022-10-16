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

    def __sub__(self, other):
        match other:
            case Vector():
                return Vector(self.x - other.x, self.y - other.y)
            case _:
                raise Exception(
                    f"Second argument needs to be an Vector object you send {type(other)}"
                )
