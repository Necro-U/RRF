class grid:
    def __init__(self, grid_x: int, grid_y: int) -> None:
        self.color = "WHİTE"
        self.grid_fx, self.grid_fy = grid_x, grid_y
        self.isinitial = False
        self.islast = False
        self.isvisited = False

        def visit():
            self.isvisited = True
            self.color = "YELLOW"

        def assign_as_first():
            self.isinitial = True
            self.color = "GREEN"

        def assign_as_last():
            self.islast = True
            self.color = "RED"

        def is_clicked(grid_x: float, grid_y: float):
            col = 0 < (grid_x - self.grid_fx) < 20
            row = 0 <= (grid_y - self.grid_fy) < 20
            return col and row
