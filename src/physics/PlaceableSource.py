import abc
from typing import Dict
from typing import Callable
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.domain.Coordinates import Coordinates
from src.physics.ElectrostaticSource import FiducialElectrostaticSource

class PlaceableSource(abc.ABC):

    def __init__(self, source : FiducialElectrostaticSource , coordinate_transformer : Callable) -> None:

        self.fieldsource = source
        self._coordsTransformer = coordinate_transformer
        self.placement_data = None
        self._transformed_coords = None

    def place(self, placement_data : Dict[str, float]) -> None:
        self.placement_data = placement_data
        self._transformed_coords = None

    def _coordstransform(self, coordinates: Coordinates) -> Coordinates:

        if not self._transformed_coords:

            self._transformed_coords = self._coordsTransformer(coordinates, self.placement_data)

            return self._transformed_coords


    def get_vector_field(self, coords: Coordinates) -> VectorField:
        tcoords = self._coordsTransform(coords)
        return self.fieldsource.get_vector_field(tcoords)


    def get_scalar_field(self, coords: Coordinates) -> ScalarField:
        tcoords = self._coordsTransform(coords)
        return self.fieldsource.get_scalar_field(tcoords)
