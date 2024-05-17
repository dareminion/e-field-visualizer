import pytest
import numpy as np
from src.domain.Domain import Domain
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField
from src.domain.Coordinates import Coordinates
from src.physics.PointCharge import PointCharge
from src.physics.PlaceableSource import PlaceableSource

@pytest.fixture
def Coord_Transform():
    coord_shifter = Coordinates.translate
    def coord_translate(coords, placement_data):
        shift_x = placement_data['x']
        shift_y = placement_data['y']

        return coord_shifter(coords, shift_x, shift_y)
    return coord_translate

@pytest.fixture
def PSource_Generation(Coord_Transform):
    source = PointCharge(10)
    psource = PlaceableSource(source, Coord_Transform)
    return psource

@pytest.fixture
def Placement_Data():
    data = {'x' : 15,
            'y' : 20}
    return data

@pytest.fixture
def Sample_Coords():
    return Domain(7,7,7,7).main_coords


def test_import():
    assert True

def test_PlaceablePointSource_init(PSource_Generation):
    psource = PSource_Generation
    assert isinstance(psource, PlaceableSource)
    assert isinstance(psource._fieldsource, PointCharge)

def test_placement(PSource_Generation, Placement_Data):
    psource = PSource_Generation
    data = Placement_Data
    psource.place(data)
    assert psource._placement_data == data

def test_coord_translation(PSource_Generation, Placement_Data, Sample_Coords):
    psource = PSource_Generation
    data = Placement_Data
    psource.place(data)
    psource._coordstransform(Sample_Coords)
    pxgrid = psource._transformed_coords.x_grid
    pygrid = psource._transformed_coords.y_grid
    expected_coordinates = Coordinates.translate(Sample_Coords, 15, 20)
    expected_x = expected_coordinates.x_grid
    expected_y = expected_coordinates.y_grid
    
    assert pxgrid.shape == (7,7)
    assert pygrid.shape == (7,7)
    assert np.array_equal(pxgrid, expected_x)
    assert np.array_equal(pygrid, expected_y)

def test_get_vector_field(PSource_Generation, Placement_Data, Sample_Coords):
    psource = PSource_Generation
    data = Placement_Data
    psource.place(data)
    output = psource.get_vector_field(Sample_Coords)
    assert isinstance(output, VectorField)

def test_get_scalar_field(PSource_Generation, Placement_Data, Sample_Coords):
    psource = PSource_Generation
    data = Placement_Data
    psource.place(data)
    output = psource.get_scalar_field(Sample_Coords)
    assert isinstance(output, ScalarField)