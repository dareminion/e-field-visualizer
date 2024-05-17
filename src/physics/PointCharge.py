import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
import scipy.constants as const
import numpy as np

k_C = const.k


class PointCharge(FiducialElectrostaticSource):

    def __init__(self, charge: float) -> None:
        self.charge = charge

    
    def efield(self, x: float, y: float) -> np.ndarray:
        
        
        
        r = ((x ** 2) + (y ** 2)) ** (.5)

        if isinstance(r, np.ndarray):
            r = np.where(r == 0, np.nan, r) 

        else:
            if r == 0:
                return 0.0

        nonzero_mask = (r != 0)

        mag_factor = k_C * self.charge / r ** 3

        x_magnitude = np.where(nonzero_mask, mag_factor * x, np.nan)
        y_magnitude = np.where(nonzero_mask, mag_factor * y, np.nan)

        efield = np.array([x_magnitude, y_magnitude])

        return efield

    
    def epotential(self, x: float, y: float) -> float:

        r = ((x ** 2) + (y ** 2)) ** (.5)
        
        if isinstance(r, np.ndarray):
            r = np.where(r == 0, np.nan, r) 

        else:
            if r == 0:
                return np.nan

        electric_potential = (k_C * self.charge) / r

        return electric_potential


        