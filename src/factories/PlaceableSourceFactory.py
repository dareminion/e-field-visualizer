import abc
from typing import Callable , Dict
from src.domain.Coordinates import Coordinates
from src.physics.PlaceableSource import PlaceableSource
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
class PlaceableSourceFactory(abc.ABC):
    
    @staticmethod
    @abc.abstractmethod
    def create_field_source(*args) -> FiducialElectrostaticSource:
        pass

    @staticmethod
    @abc.abstractmethod
    def create_coord_transformer(Coords: Coordinates, Placement_Data : Dict[str, float]) -> Callable[..., Coordinates]:
        pass
    
    @abc.abstractmethod
    def create_placeable_source(self, *args, Coords: Coordinates, Placement_Data : Dict[str, float]) -> PlaceableSource:
        field_source = self.create_field_source(*args)
        coord_transformer = self.create_coord_transformer(Coords, Placement_Data)
        return PlaceableSource(field_source, coord_transformer)



