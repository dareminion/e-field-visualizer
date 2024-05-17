import abc
import numpy as np
from src.math.ScalarFields import ScalarField

class ScalarFieldSource(abc.ABC):
    '''
    Protocol for a Source to ensure Scalar Field Generation
    '''

    @abc.abstractmethod
    def get_scalar_field(self, x_coords : np.ndarray, y_coords : np.ndarray) -> ScalarField:
        pass
    