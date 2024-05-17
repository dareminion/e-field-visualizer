import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
import numpy as np

class FiducialElectrostaticSource(abc.ABC):
    @abc.abstractmethod
    def efield(self, x: float, y: float) -> np.ndarray:
        pass


        
    @abc.abstractmethod
    def epotential(self, x: float,y: float)-> float:
        pass