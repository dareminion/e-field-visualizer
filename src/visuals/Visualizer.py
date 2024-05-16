import numpy as np
import matplotlib.pyplot as plt
from src.domain.Domain import Domain

class Visualizer:

    # Creates a default plot of a pre-determined size that can be changed later
    def __init__(self, figsize: tuple=(10,10)) -> None:
        self.figure, self.axes = plt.subplots(figsize=figsize)

    # Plot a vector field with arrows
    def plot_vector_field(self, vector_field, label='Vector Field', color='r'):

        # Create a meshgrid for the vector field
        X, Y = np.meshgrid(np.arange(vector_field.shape[1]), np.arange(vector_field.shape[0]))

        # Extract the x and y components of the vector field
        Ex = vector_field[:, :, 0]
        Ey = vector_field[:, :, 1]

        # Plot the vector field using quiver
        self.axes.quiver(X, Y, Ex, Ey, color=color, label=label)
        self.axes.set_title('Vector Field')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')
        self.axes.grid()

        if label:
            self.axes.legend()
    
    # Plot a scalar field as a heatmap
    def plot_scalar_field(self, scalar_field, label='Electric Potential', cmap='viridis'):

        # Plot the scalar field using imshow
        heatmap = self.axes.imshow(scalar_field, extent=(0, scalar_field.shape[1], 0, scalar_field.shape[0]), origin='lower', cmap=cmap, alpha=0.6)
        
        # Add a color bar to the heatmap
        cbar = self.figure.colorbar(heatmap, ax=self.axes, label=label)
        cbar.set_alpha(1)
        cbar._draw_all()

    # Display the plot
    def show(self):
        plt.show()
