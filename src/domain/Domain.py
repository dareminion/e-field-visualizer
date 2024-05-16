import numpy as np

class Domain:
    '''
    Coordinates Class
       .x (meshgrid)
       .y (meshgrid)
       shape
    '''
    def __init__(self, x_span: int, y_span: int, num_x_coords: int, num_y_coords: int) -> None:
        
        # x - span
        self.x_span = x_span

        # y - span
        self.y_span = y_span

        # x - num of coords
        self.num_x_coords = num_x_coords
        
        # y - num of coords
        self.num_y_coords = num_y_coords
        
        self.main_coords = self._domain_setup()
        

    def _domain_setup(self) -> tuple:
        
        # Determine min & max values
        x_min, x_max = (self.x_span * -1) / 2, self.x_span / 2
        y_min, y_max = (self.y_span * -1) / 2, self.y_span / 2

        # Create x and y coordinates
        x_coords = np.linspace(x_min, x_max, self.num_x_coords)
        y_coords = np.linspace(y_min, y_max, self.num_y_coords)

        # Generate grid using np.meshgrid
        return  Coordinates(np.meshgrid(x_coords, y_coords))

        # # Use np.vstack to help visualize grid points (Could be useful later)
        # grid_points = np.vstack([x_grid.ravel(), y_grid.ravel()]).T

        
