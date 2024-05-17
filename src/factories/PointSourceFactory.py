from typing import Callable, Dict
from src.domain.Coordinates import Coordinates
from src.physics.PlaceableSource import PlaceableSource
from src.factories.PlaceableSourceFactory import PlaceableSourceFactory
from src.physics.PointCharge import PointCharge

class PointSourceFactory(PlaceableSourceFactory):
    
    @staticmethod
    def create_field_source(charge : float) -> PointCharge:
        return PointCharge(charge)
    
    @staticmethod
    def create_coord_transformer(Coords: Coordinates, Placement_Data: Dict[str, float]) -> Callable[..., Coordinates]:
        def coord_translator():
            shift_x = Placement_Data['x']
            shift_y = Placement_Data['y']
            return Coordinates.translate(Coords, shift_x, shift_y)
        return coord_translator
    
    def create_placeable_source(self, charge : float, Coords: Coordinates, Placement_Data: Dict[str, float]) -> PlaceableSource:
        field_source = self.create_field_source(charge)
        coord_transformer = self.create_coord_transformer(Coords, Placement_Data)
        return PlaceableSource(field_source, coord_transformer)