import pytest
from src.physics.PlaceableSource import PlaceableSource
from src.factories.PointSourceFactory import PointSourceFactory
from src.domain.Domain import Domain

@pytest.fixture
def Placement_Data():
    data = {'x' : 15,
            'y' : 20}
    return data

@pytest.fixture
def Sample_Coords():
    return Domain(7,7,7,7).main_coords

def test_psource_factory(Placement_Data, Sample_Coords):
    factory = PointSourceFactory()
    test_placeable_source = factory.create_placeable_source(10, Sample_Coords, Placement_Data)
    assert isinstance(test_placeable_source, PlaceableSource)