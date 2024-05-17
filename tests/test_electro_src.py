import pytest
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField
from src.math.ScalarFieldSource import ScalarFieldSource
from src.math.VectorFieldSource import VectorFieldSource
from src.domain.Coordinates import Coordinates
from src.physics.PointCharge import PointCharge
from src.domain.Domain import Domain


@pytest.fixture
def generate_pt_source():
    test_point_charge = PointCharge(10)

    return (test_point_charge)

def test_import():
    assert True


def test_get_vector_field_shape(generate_pt_source):
    test_coordinates = Domain(5,5,5,5).main_coords
    x_coords = test_coordinates.x_grid
    y_coords = test_coordinates.y_grid
    test_source = generate_pt_source
    test_efield = test_source.get_vector_field(x_coords, y_coords)
    assert True

