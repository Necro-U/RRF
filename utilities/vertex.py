from utilities.vector import Vector


class Vertex:
    def __init__(self, position: Vector) -> None:
        self.position = position
        self.is_initial = False
        self.is_last = False
        self.parent_vertex: Vertex = None
        self.children_vertexes: list[Vertex] = []

    def get_pos(self) -> list:
        return self.position.pos

    def make_initial(self):
        self.is_initial = True

    def make_last(self):
        self.is_last = True

    def add_child(self, vertex):
        self.children_vertexes.append(vertex)

    def __sub__(self, other: object):
        return self.position - other.position
