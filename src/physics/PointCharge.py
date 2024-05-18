import numpy as np
import scipy.constants as const
from src.physics.ElectrostaticSource import FiducialElectrostaticSource


k_C = 1 / (4 * const.pi * const.epsilon_0)

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
        if isinstance(r, np.ndarray):
        
            return np.stack(efield, axis = 2)

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


        