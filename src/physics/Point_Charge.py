import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.physics.Electrostatic_Source import FiducialElectrostaticSource
import scipy.constants as const
import numpy as np

k_C = const.Coulomb

class ElectrostaticPtCharge(FiducialElectrostaticSource):

    def electric_field(self, coordinates: Coordinates) -> VectorField:
        
        # x and y coordinates in numpy arrays
        x = coordinates.x_grid
        y = coordinates.y_grid

        r = ((x ** 2) + (y ** 2)) ** 1/2

        x_magnitude = (((k_c) * q) / r ** 2 ) * (x/r)
        y_magnitude = (((k_c) * q) / r ** 2 ) * (y/r)

        efield = np.dstack(x_magnitude, y_magnitude)

        return efield

        