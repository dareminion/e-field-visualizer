import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
import scipy.constants as const
import numpy as np

k_C = const.Coulomb

class ElectrostaticPtCharge(FiducialElectrostaticSource):

    def variables(coordinates: Coordinates) -> tuple:

        # x and y coordinates in numpy arrays
        x = coordinates.x_grid
        y = coordinates.y_grid

        r = ((x ** 2) + (y ** 2)) ** 1/2

        return x,y,r

    def electric_field(self, coordinates: Coordinates) -> VectorField:
        
        x,y,r = variables(coordinates)

        x_magnitude = (((k_c) * q) / r ** 2 ) * (x/r)
        y_magnitude = (((k_c) * q) / r ** 2 ) * (y/r)

        efield = np.dstack(x_magnitude, y_magnitude)

        return VectorField(efield)

    def epotential(self, coordinates: Coordinates) -> ScalarField:

        x,y,r = variables(coordinates)

        electric_potential = (k_C * q) / r

        return ScalarField(electric_potential)


        