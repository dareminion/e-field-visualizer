import numpy as np
import matplotlib.pyplot as plt
from src.domain.Domain import Domain
from src.physics.PointCharge import PointCharge
from src.physics.PlaceableSource import PlaceableSource
from matplotlib.pyplot import quiver, streamplot, pcolormesh, contour

class Visualizer:

    # Creates a default plot of a pre-determined size that can be changed later
    def __init__(self, domain: Domain) -> None:
        
        self.X = domain.main_coords.x_grid
        self.Y = domain.main_coords.y_grid

        self._shape = domain.main_coords.shape
    
        # self.figure is a new figure that gets generated at each instantiation
        # self.axes are a pair of axes (subplots) that get generated at each instantiation
        self.figure, self.axes = plt.subplots(figsize=self._shape)
        # self.figure, self.axes = plt.subplots(figsize=(domain.x_span, domain.y_span))

        self.REGISTRY = {'Vector Fields' : {'quiver' : getattr(self.axes, 'quiver'),
                                        'fieldlines' : getattr(self.axes, 'streamplot')},
                    
                    'Scalar Fields' : {'heatmap' : getattr(self.axes, 'pcolormesh'),
                                        'grayscale' : getattr(self.axes, 'pcolormesh'),
                                        'contourmap' : getattr(self.axes, 'contour') }
                }

    # Plot a vector field with arrows
    def plot_vector_field(self, vector_field, plot_type):

        plot_func = self.REGISTRY['Vector Fields'][plot_type]

        Ex = vector_field[:, :, 0]
        Ey = vector_field[:, :, 1]

        magnitude = np.sqrt(Ex**2 + Ey**2)
        Ex = Ex / magnitude
        Ey = Ey / magnitude

        if plot_type == 'quiver':
            plot_func(self.X, self.Y, Ex, Ey, color='r', label='Vector Field')

        elif plot_type == 'fieldlines':
            plot_func(self.X, self.Y, Ex, Ey, color='r')

        self.axes.set_title('Vector Field')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid()

        if plot_type == 'quiver':
            self.axes.legend()

    
    # Plot a scalar field as a heatmap
    def plot_scalar_field(self, scalar_field, plot_type):

        plot_func = self.REGISTRY['Scalar Fields'][plot_type]

        if plot_type == 'heatmap':
            c = plot_func(self.X, self.Y, scalar_field, cmap='viridis')

        elif plot_type == 'grayscale':
            c = plot_func(self.X, self.Y, scalar_field, cmap='gray')

        elif plot_type == 'contourmap':
            c = plot_func(self.X, self.Y, scalar_field, cmap='viridis')

        cbar = self.figure.colorbar(c, ax=self.axes, label='Electric Potential')
        cbar.set_alpha(1)
        cbar._draw_all()

    # Display the plot
    def show(self):
        plt.show()

    def place_source(self, source: PlaceableSource) -> None:

        if isinstance(source._fieldsource, PointCharge):
            x, y = source._placement_data['x'], source._placement_data['y']
            self.axes.plot(x, y, 'bo', markersize=10, label='Source')
            self.axes.legend()
        else:
            raise ValueError("Source type not compatible")
