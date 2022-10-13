from dataclasses import dataclass
from math import sqrt


@dataclass(slots=True, repr=False)
class Vector:
    pos: list

    @property
    def distance(self):
        return sqrt(self.pos[0] ** 2 + self.pos[1] ** 2)

    def __sub__(self, other):
        match other:
            case Vector(pos):
                return Vector([self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]])
            case _:
                raise Exception(
                    f"Second argument needs to be an Vector object you send {type(other)}"
                )
