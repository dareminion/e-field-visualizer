import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
import scipy.constants as const
import numpy as np

k_C = 8.99 * (10 ** 9)

class ElectrostaticPtCharge(FiducialElectrostaticSource):


    def electric_field(self, x, y):
        
        r = ((x ** 2) + (y ** 2)) ** 1/2

        if r == 0:
            return 0

        else:
            x_magnitude = (((k_C) * q) / r ** 2 ) * (x/r)
            y_magnitude = (((k_C) * q) / r ** 2 ) * (y/r)

        efield = np.arry((x_magnitude, y_magnitude))

        return VectorField(efield)

    def electric_potential(self, x, y):

        r = ((x ** 2) + (y ** 2)) ** 1/2

        if r == 0:
            return 0
        
        else:
            electric_potential = (k_C * q) / r

        return ScalarField(electric_potential)


        