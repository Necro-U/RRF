from random import randint
import sys, pygame
from utilities.VertexManager import VertexManager
from utilities.color import Color
from utilities.grid import Grid
from pygame import Rect, Surface
from utilities.vector import Vector

from utilities.vertex import Vertex

pygame.init()
size = width, height = 600, 600
speed = [1, 1]
black = 0, 0, 0


# grid items
grid_list: list[list[Grid]] = []
grid_rate = 20


# selecting items
selected_count = 0


screen = pygame.display.set_mode(size)


# Vector Manager
manager = VertexManager(screen, width, height)

# Local functions
def line_drawer():
    for i in range(0, width, grid_rate):
        pygame.draw.line(screen, Color.GREY, (0, i), (width, i), width=2)
    for j in range(0, height, grid_rate):
        pygame.draw.line(screen, Color.GREY, (j, 0), (j, height), width=2)


def grid_drawer():
    for row in grid_list:
        for item in row:
            pygame.draw.rect(
                screen, item.color, Rect(item.grid_x, item.grid_y, grid_rate, grid_rate)
            )


def grid_mouse_handler(count: int, x: int, y: int):
    for row in grid_list:
        for item in row:
            if item.isclicked(x, y):
                if count == 0:
                    item.assign_as_first()
                elif count == 1:
                    item.assign_as_last()
                # else:
                #     item.visit()
                print(item.color, item.start_coordinate, item.finish_coordinate)


def create_grids(grid_list: list[list[Grid]]):
    for i in range(0, height, grid_rate):
        temp = []
        temp_rect = []
        for j in range(0, width, grid_rate):
            grid = Grid((i, j), grid_rate)
            temp.append(grid)
        grid_list.append(temp)


# Creating grids
# create_grids(grid_list)


# Non-grid functions

# define a class
def mouse_handler(root: Surface, pos: tuple[int, int], selected: int):
    if selected == 0:
        pygame.draw.circle(root, Color.GREEN, pos, 5)
    elif selected == 1:
        pygame.draw.circle(root, Color.RED, pos, 5)


def rrf(start: Vertex, end: Vertex):
    manager.add_vertex(start)
    # manager.add_vertex(end)

    x = randint(0, width)
    y = randint(0, height)
    print(x, y)
    manager.add_vertex(Vertex(Vector([x, y])))


rrf_starter = False


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            pos = [x, y]
            # print(x, y)
            mouse_handler(screen, pos, selected_count)
            # grid_mouse_handler(selected_count)
            if selected_count != 2:
                match selected_count:
                    case 0:
                        print(pos)
                        start = pos
                    case 1:
                        print(pos)
                        end = pos
                selected_count += 1
            else:
                rrf_starter = True

    if rrf_starter:
        manager.start_rrf(start, end)
    # Grid Funcsions
    # grid_drawer()
    # line_drawer()

    pygame.display.flip()
