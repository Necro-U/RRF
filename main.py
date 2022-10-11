import sys, pygame
from utils.grid import Grid
from utils.color import Color
from pygame import Rect

pygame.init()
size = width, height = 620, 620
speed = [1, 1]
black = 0, 0, 0

# grid items
grid_list: list[list[Grid]] = []
grid_rate = 20


# selecting items
selected_count = -1


screen = pygame.display.set_mode(size)

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


def mouse_handler(count: int):
    for row in grid_list:
        for item in row:
            if item.isclicked(x, y):
                if count == 0:
                    item.assign_as_first()
                elif count == 1:
                    item.assign_as_last()
                else:
                    item.visit()
                print(item.color, item.start_coordinate, item.finish_coordinate)


# Creating grids

for i in range(0, height, grid_rate):
    temp = []
    temp_rect = []
    for j in range(0, width, grid_rate):
        grid = Grid(
            (i, j),
        )
        temp.append(grid)
    grid_list.append(temp)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            mouse_handler(selected_count)
            if selected_count != 3:
                selected_count += 1

    grid_drawer()
    line_drawer()
    pygame.display.flip()
