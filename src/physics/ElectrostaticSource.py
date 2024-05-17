import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField 
from src.math.ScalarFields import ScalarField
from src.math.VectorFieldSource import VectorFieldSource
from src.math.ScalarFieldSource import ScalarFieldSource
import numpy as np

class FiducialElectrostaticSource(VectorFieldSource, ScalarFieldSource):
    @abc.abstractmethod
    def efield(self, x: float, y: float) -> np.ndarray:
        pass

    @abc.abstractmethod
    def epotential(self, x: float,y: float)-> float:
        pass

    
    def get_vector_field(self, x_coords: np.ndarray, y_coords: np.ndarray) -> VectorField:
        efield = self.efield(x_coords, y_coords)
        return VectorField(efield)

    
    def get_scalar_field(self, x_coords: np.ndarray, y_coords: np.ndarray) -> ScalarField:
        epotential = self.epotential(x_coords, y_coords)
        return ScalarField(epotential)

    