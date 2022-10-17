from math import sqrt
from random import randint
from time import sleep
from utilities.color import Color
from utilities.vector import Vector
from utilities.vertex import Vertex
from pygame.surface import Surface
from threading import RLock, Thread
from utilities.globals import RADIUS
import pygame


class VertexManager:
    def __init__(self, root: Surface, width: int, height: int) -> None:
        self.vertex_list: list[Vertex] = []
        self.root = root
        self.width = width
        self.height = height
        self.rrf_finisher = False
        self.aim: Vertex | None = None
        self.max_dist = 50

    def finish(self, vertex: Vertex):
        self.rrf_finisher = True
        self.aim = vertex

    def add_vertex(self, vertex: Vertex):
        if not len(self.vertex_list):
            return
        # parent = self.find_closest_vertex(vertex)
        # print(parent)
        if vertex.parent_vertex == None:
            return
        # parent.add_child(vertex)
        # vertex.parent_vertex = parent
        self.vertex_list.append(vertex)

    # Needs to be changed
    def draw_lines(self, lock: RLock):
        # with lock:

        if not self.rrf_finisher:
            for vertex in self.vertex_list:
                for each in vertex.children_vertexes:
                    # print(f"vertex list {self.vertex_list}")
                    pygame.draw.line(
                        self.root,
                        Color.PURPLE,
                        vertex.get_pos(),
                        each.get_pos(),
                        width=2,
                    )
        else:
            temp = self.aim
            while temp and temp.parent_vertex != None:
                pygame.draw.line(
                    self.root,
                    Color.GREEN,
                    temp.position.pos,
                    temp.parent_vertex.position.pos,
                    width=2,
                )
                pygame.draw.circle(self.root, Color.YELLOW, temp.position.pos, 3)
                temp = temp.parent_vertex

    def find_closest_vertex(self, new_vertex: Vertex) -> Vertex:
        key = lambda x: (x - new_vertex).distance
        closest = min(self.vertex_list, key=key)

        return closest

    def __modifier(self, initial: Vertex, aim: Vertex):
        x, y = initial.get_pos()
        direction = initial.position.direction(aim.position)

        ara_vertex = Vertex(
            x - int(direction.x * self.max_dist),
            y - int(direction.y * self.max_dist),
            parent=initial,
        )

        return ara_vertex

    def __control_vertex(self, closest: Vertex, to: Vertex):
        distance = (to - closest).distance
        if distance < self.max_dist:
            return to
        return self.__modifier(closest, to)

    def start_rrf(self, start_point: list[int], end_point: list[int], lock: RLock):

        x_s, y_s = start_point
        if not self.rrf_finisher:
            self.vertex_list.append(Vertex(x_s, y_s, isinitial=True))
            pos = x, y = [randint(0, self.width), randint(0, self.height)]

            while pos != end_point:
                # sleep(0.1)

                with lock:

                    new = Vertex(x, y)
                    closest = self.find_closest_vertex(new)
                    new = self.__control_vertex(closest, new)
                    closest.add_child(new)
                    new.set_parent(closest)
                    #     continue

                    dist_from_end = sqrt(
                        (pos[0] - end_point[0]) ** 2 + (pos[1] - end_point[1]) ** 2
                    )
                    if dist_from_end <= RADIUS:
                        print("endğpos", pos)
                        self.finish(new)
                        self.add_vertex(new)
                        break
                    self.add_vertex(new)
                    pos = x, y = [randint(0, self.width), randint(0, self.height)]
