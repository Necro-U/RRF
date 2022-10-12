from .color import Color

# TODO grids needs to have neighbours


class Grid:
    def __init__(self, coordinate: tuple, grid_rate) -> None:
        self.color = Color.WHITE
        self.start_coordinate = self.grid_x, self.grid_y = coordinate
        self.isinitial = False
        self.islast = False
        self.isvisited = False
        self.grid_rate = grid_rate
        self.finish_coordinate = (
            self.start_coordinate[0] + grid_rate,
            self.start_coordinate[1] + grid_rate,
        )

    def visit(self):
        self.isvisited = True
        self.color = Color.YELLOW

    def assign_as_first(self):
        self.isinitial = True
        self.color = Color.GREEN

    def assign_as_last(self):
        self.islast = True
        self.color = Color.RED

    def isclicked(self, grid_x: int, grid_y: int):
        col = 0 <= (grid_x - self.grid_x) and (grid_x - self.grid_x) < self.grid_rate
        row = 0 <= (grid_y - self.grid_y) and (grid_y - self.grid_y) < self.grid_rate
        return col and row
