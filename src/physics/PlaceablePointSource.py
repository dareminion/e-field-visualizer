import abc
from typing import Dict
from typing import Callable
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.domain.Coordinates import Coordinates
from src.physics.PlaceableSource import PlaceableSource
from src.physics.ElectrostaticSource import FiducialElectrostaticSource

class PlaceablePointSource(PlaceableSource):

    def _coordstransform(self, coordinates: Coordinates) -> Coordinates:

        if not self._transformed_coords:

            self._transformed_coords = self._coordsTransformer(coordinates, self._placement_data)

            return self._transformed_coords

