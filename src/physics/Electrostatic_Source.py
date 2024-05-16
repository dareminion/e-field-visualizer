import abc
from src.domain.Coordinates import Coordinates
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField

COLUMBS_CONSTANT = 8.99 * (10 ** 9)

class FiducialElectrostaticSource(abc.ABC):
    def __init__(self, charge: float, placement_data: dict) -> None:
        self.charge = charge
        self.placement_data = placement_data


    @abstractmethod
    def electric_field(self, coordinates: Coordinates) -> VectorField:
        pass

        
    @abstractmethod
    def electric_potential(self, coordinates: Coordinates)-> ScalarField:
        pass