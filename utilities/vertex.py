from utilities.vector import Vector


class Vertex:
    def __init__(self, x: int, y: int, isinitial=False, parent=None) -> None:
        self.position = Vector(x, y)
        self.is_initial = isinitial
        self.parent_vertex: Vertex | None = parent
        self.children_vertexes: list[Vertex] = []

    def get_pos(self) -> list:
        return self.position.pos

    def add_child(self, vertex):
        self.children_vertexes.append(vertex)

    def set_parent(self, parent):
        self.parent_vertex = parent

    def __sub__(self, other: object):
        match other:
            case Vertex():
                return self.position - other.position
            case _:
                raise Exception("Wrong type")
