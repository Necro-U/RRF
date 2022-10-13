from utilities.vector import Vector


class Vertex:
    def __init__(self, position: Vector, isinitial=False) -> None:
        self.position = position
        self.is_initial = isinitial
        self.parent_vertex: Vertex = None
        self.children_vertexes: list[Vertex] = []

    def get_pos(self) -> list:
        return self.position.pos

    def add_child(self, vertex):
        self.children_vertexes.append(vertex)

    def __sub__(self, other: object):
        return self.position - other.position
