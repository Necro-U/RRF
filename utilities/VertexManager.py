from random import randint
from time import sleep
from utilities.color import Color
from utilities.vertex import Vertex
from pygame.surface import Surface
from threading import RLock, Thread
import pygame


class VertexManager:
    def __init__(self, root: Surface, width: int, height: int) -> None:
        self.vertex_list: list[Vertex] = []
        self.root = root
        self.width = width
        self.height = height
        self.rrf_finisher = False
        self.aim: Vertex | None = None
        self.max_dist = 100

    def finish(self, vertex: Vertex):
        self.rrf_finisher = True
        self.aim = vertex

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

    # Needs to be changed
    def draw_lines(self, lock: RLock):
        with lock:

            if not self.rrf_finisher:
                for vertex in self.vertex_list:
                    if not vertex.children_vertexes:
                        continue

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

    def find_closest_vertex(self, new_vertex: Vertex) -> Vertex | None:
        if len(self.vertex_list) < 1:
            return None
        key = lambda x: (x - new_vertex).distance
        closest = min(self.vertex_list, key=key)
        distance = (new_vertex - closest).distance
        # print(closest.position.pos)
        # TODO! : distance fazla olursa modifite et!!
        if distance < self.max_dist:
            return closest
        return None

    # TODO Maximum uzaklık ekle
    def start_rrf(self, start_point: list[int], end_point: list[int], lock: RLock):

        x_s, y_s = start_point
        if not self.rrf_finisher:
            self.vertex_list.append(Vertex(x_s, y_s, isinitial=True))
            pos = x, y = [randint(0, self.width), randint(0, self.height)]
            while pos != end_point:
                sleep(0.1)

                with lock:

                    new = Vertex(x, y)
                    closest = self.find_closest_vertex(new)
                    if closest:
                        closest.add_child(new)
                        new.set_parent(closest)
                        #     continue

                    if pos == end_point:
                        print("endğpos", pos)
                        self.finish(new)
                    #     break
                    self.add_vertex(new)

    def run(self, start_point: list[int], end_point):
        func = Thread(target=self.start_rrf, args=[start_point, end_point])
        func.start()
