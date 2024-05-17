import abc
from typing import Dict
from typing import Callable
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.domain.Coordinates import Coordinates
from src.physics.ElectrostaticSource import FiducialElectrostaticSource

class PlaceableSource():

    def __init__(self, source : FiducialElectrostaticSource , coordinate_transformer : Callable) -> None:
        self._fieldsource = source
        self._coordsTransformer = coordinate_transformer
        self._placement_data = None
        self._transformed_coords = None


    def place(self, placement_data: Dict [str, float]) -> None:
        self._placement_data = placement_data
        self.transformed_coords = None

    def _coordstransform(self, coordinates: Coordinates) -> Coordinates:

        if not self._transformed_coords:

            self._transformed_coords = self._coordsTransformer(coordinates, self._placement_data)

            return self._transformed_coords
        else:
            return self._transformed_coords

    def get_vector_field(self, coords: Coordinates) -> VectorField:
        tcoords = self._coordstransform(coords)
        return self._fieldsource.get_vector_field(tcoords.x_grid, tcoords.y_grid)


    def get_scalar_field(self, coords: Coordinates) -> ScalarField:
        tcoords = self._coordstransform(coords)
        return self._fieldsource.get_scalar_field(tcoords.x_grid, tcoords.y_grid)