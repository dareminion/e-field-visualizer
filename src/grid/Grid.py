import numpy as np

class Grid:

    def __init__(self, x_span: int, y_span: int, x_spacing: int, num_y_points: int) -> None:
        
        # x - value
        self.x_span = x_span

        # y - value
        self.y_span = y_span

        # x - scaling
        self.x_spacing = x_spacing
        
        # y - scaling
        self.y_spacing = num_y_points

    def make_grid(self) -> None:
        pass
