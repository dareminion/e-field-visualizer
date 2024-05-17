import numpy as np
class Coordinates:

    def __init__(self, x_grid: np.ndarray , y_grid: np.ndarray) -> None:

        self.x_grid = x_grid
        self.y_grid = y_grid

        # Determines the coordinate shape
        if x_grid.shape == y_grid.shape:
            self.shape = x_grid.shape
        else:
            raise ValueError("The X and Y meshgrids are not the same shape")


    def translate(self, h: int, k: int) -> 'Coordinates':
        
        # Shifts the coordinates
        new_x_grid = self.x_grid - h
        new_y_grid = self.y_grid - k

        # Creates new shifted Coordinates object
        return Coordinates(new_x_grid, new_y_grid)
    
    def rotate(self, theta: float) -> 'Coordinates':
        pass


