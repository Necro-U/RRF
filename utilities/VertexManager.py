from random import randint
from utilities.color import Color
from utilities.vector import Vector
from utilities.vertex import Vertex
from pygame import Surface
import pygame


class VertexManager:
    def __init__(self, root: Surface, width: int, height: int) -> None:
        self.vertex_list: list[Vertex] = []
        self.root = root
        self.width = width
        self.height = height
        self.rrf_finisher = False

    def add_vertex(self, vertex: Vertex):
        if not len(self.vertex_list):
            return
        parent = self.find_closest_vertex(vertex)
        # print(parent)
        if parent == None:
            return
        parent.add_child(vertex)
        vertex.parent_vertex = parent
        self.vertex_list.append(vertex)

    def draw_lines(self):
        for vertex in self.vertex_list:
            if not vertex.children_vertexes:
                continue

            for each in vertex.children_vertexes:
                # print(f"vertex list {self.vertex_list}")
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

    def start_rrf(self, start_point: list, end_point: list):
        if not self.rrf_finisher:
            self.vertex_list.append(Vertex(Vector(start_point), isinitial=True))
            pos = [randint(0, self.width), randint(0, self.height)]
            new = Vertex(Vector(pos))
            closest = self.find_closest_vertex(new)
            if closest:
                closest.add_child(new)
                #     continue

            if pos == end_point:
                print("endğpos", pos)
                self.rrf_finisher = True
            #     # self.finis() # we can change the colors
            #     break
            self.add_vertex(new)
        else:
            # the looking up logic need to be change
            # while new.parent != None :
            print("finded")

        self.draw_lines()
