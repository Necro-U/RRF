from utilities.color import Color
from utilities.vector import Vector
from utilities.vertex import Vertex
from pygame import Surface
import pygame


class VertexManager:
    def __init__(self, root: Surface) -> None:
        self.vertex_list: list[Vertex] = []
        self.root = root

    def add_vertex(self, vertex: Vertex):
        parent = self.find_closest_vertex(vertex)
        parent.add_child(vertex)
        vertex.parent_vertex = parent
        self.vertex_list.append(vertex)

    def draw_lines(self):
        for vertex in self.vertex_list:
            if not vertex.children_vertexes:
                continue
            for each in vertex.children_vertexes:
                pygame.draw.line(
                    self.root, Color.PURPLE, vertex.get_pos(), each.get_pos(), width=2
                )

    def find_closest_vertex(self, new_vertex: Vertex) -> Vertex:
        if len(self.vertex_list) <= 1:
            return None
        key = lambda x: (x - new_vertex).distance
        closest = min(self.vertex_list, key=key)
        # print(closest.position.pos)
        return closest
