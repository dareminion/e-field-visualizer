import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
import scipy.constants as const
import numpy as np

k_C = 8.99 * (10 ** 9)

class PointCharge(FiducialElectrostaticSource):

    def __init__(self, charge: float) -> None:
        self.charge = charge

    
    def efield(self, x: float, y: float) -> np.ndarray:
        
        r = ((x ** 2) + (y ** 2)) ** (.5)

        if r == 0:
            return np.array([0,0])

        else:
            x_magnitude = (((k_C) * self.charge) / r ** 2 ) * (x/r)
            y_magnitude = (((k_C) * self.charge) / r ** 2 ) * (y/r)

        efield = np.array([x_magnitude, y_magnitude])

        return efield

    
    def epotential(self, x: float, y: float) -> float:

        r = ((x ** 2) + (y ** 2)) ** (.5)

        if r == 0:
            return 0
        
        else:
            electric_potential = (k_C * self.charge) / r

        return electric_potential


        