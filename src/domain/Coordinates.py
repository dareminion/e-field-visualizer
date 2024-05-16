import numpy as np
class Coordinates:

    def __init__(self, x_grid, y_grid) -> None:

        self.x_grid = x_grid
        self.y_grid = y_grid

        # Determines the coordinate shape
        if x_grid.shape == y_grid.shape:
            self.shape = x_grid.shape
        else:
            raise ValueError("The X and Y meshgrids are not the same shape")

        
