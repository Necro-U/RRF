from utils.color import Color


class Grid:
    def __init__(
        self,
        coordinate: tuple,
    ) -> None:
        self.color = Color.WHITE
        self.start_coordinate = self.grid_x, self.grid_y = coordinate
        self.isinitial = False
        self.islast = False
        self.isvisited = False
        self.finish_coordinate = (
            self.start_coordinate[0] + 20,
            self.start_coordinate[1] + 20,
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
        col = 0 <= (grid_x - self.grid_x) and (grid_x - self.grid_x) < 20
        row = 0 <= (grid_y - self.grid_y) and (grid_y - self.grid_y) < 20
        return col and row
