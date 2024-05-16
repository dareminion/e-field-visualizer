import numpy as np
from src.domain.Coordinates import Coordinates
from src.physics.placeablesource import PlaceableSource
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField

class Domain:

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
        x_grid, y_grid = np.meshgrid(x_coords, y_coords)
        return Coordinates(x_grid, y_grid)

        # # Use np.vstack to help visualize grid points (Could be useful later)
        # grid_points = np.vstack([x_grid.ravel(), y_grid.ravel()]).T

    # Returns VectorField
    def get_efield(self, source: PlaceableSource, coords: Coordinates) -> VectorField:
        
        return source.get_efield(coords)

    # Returns ScalarField
    def get_epotential(self, source: PlaceableSource, coords: Coordinates) -> ScalarField:
        
        return source.get_epotential(coords)
        
