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
        
        # Translates the coordinates
        new_x_grid = self.x_grid - h
        new_y_grid = self.y_grid - k

        # Creates new translated Coordinates object
        return Coordinates(new_x_grid, new_y_grid)
    
    def rotate(self, theta: float) -> 'Coordinates':

        # Defines the rotation matrix
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        # Flatten the grids and stack for matrix multiplication
        original_coords = np.stack((self.x_grid.ravel(), self.y_grid.ravel()), axis=1)  # Shape: (n*m, 2)

        # Apply the rotation matrix to each coordinate pair
        rotated_coords = original_coords @ rotation_matrix.T

        # Reshape back to grid shape
        new_x_grid = rotated_coords[:, 0].reshape(self.x_grid.shape)
        new_y_grid = rotated_coords[:, 1].reshape(self.y_grid.shape)

        return Coordinates(new_x_grid, new_y_grid)


