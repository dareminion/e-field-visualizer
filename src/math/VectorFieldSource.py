import abc
import numpy as np
from src.math.VectorFields import VectorField

class VectorFieldSource(abc.ABC):
    '''
    Protocol to ensure Vector Field generation from a source
    '''

    @abc.abstractmethod
    def get_vector_field(self, x_coords: np.ndarray, y_coords: np.ndarray) -> VectorField:
        pass