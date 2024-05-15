import numpy as np

class Grid:

    def __init__(self, x_span: int, y_span: int, num_x_coords: int, num_y_coords: int) -> None:
        
        # x - value
        self.x_span = x_span

        # y - value
        self.y_span = y_span

        # x - spacing
        self.num_x_coords = num_x_coords
        
        # y - spacing
        self.num_y_coords = num_y_coords


    def _grid_setup(self) -> tuple:
        
        # Determine min & max values
        x_min, x_max = (self.x_span * -1) / 2, self.x_span / 2
        y_min, y_max = (self.y_span * -1) / 2, self.y_span / 2

        # Create x and y coordinates
        x_coords = np.linspace(x_min, x_max, self.num_x_coords)
        y_coords = np.linspace(y_min, y_max, self.num_y_coords)

        return x_coords, y_coords


    def make_grid(self) -> tuple:
        
        # Get x and y coordinates
        x_coords, y_coords = self._grid_setup()

        # Generate grid using np.meshgrid
        x_grid, y_grid = np.meshgrid(x_coords, y_coords)

        # # Use np.vstack to help visualize grid points (Could be useful later)
        # grid_points = np.vstack([x_grid.ravel(), y_grid.ravel()]).T

        return x_grid, y_grid
