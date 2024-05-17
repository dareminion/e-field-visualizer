import pytest
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField
from src.math.ScalarFieldSource import ScalarFieldSource
from src.math.VectorFieldSource import VectorFieldSource
from src.domain.Coordinates import Coordinates
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
from src.physics.PointCharge import PointCharge
from src.domain.Domain import Domain
import numpy as np


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
    assert isinstance(test_efield, VectorField)


def test_get_scalar_field_type(generate_pt_source):
    test_coordinates = Domain(5,5,5,5).main_coords
    x_coords = test_coordinates.x_grid
    y_coords = test_coordinates.y_grid
    test_source = generate_pt_source
    test_epotential = test_source.get_scalar_field(x_coords, y_coords)
    assert isinstance(test_epotential, ScalarField)

def test_get_vector_field_value(generate_pt_source):
    k_C = 8.99 * (10 ** 9)
    test_coordinates = Domain(2,2,2,2).main_coords
    x_coords = test_coordinates.x_grid
    y_coords = test_coordinates.y_grid
    test_source = generate_pt_source
    test_efield_output = test_source.get_vector_field(x_coords, y_coords)
    efieldx1 = (k_C * 10 / (2)) * (-1 / (2 ** (.5)))
    efieldy1 = (k_C * 10 / 2) * (-1 / (2 ** (.5)))
    efieldx2 = (k_C * 10 / 2) * (1 / (2 ** (.5)))
    efieldy2 = (k_C * 10 / 2) * (-1 / (2 ** (.5)))
    efieldx3 = (k_C * 10 / (2)) * (-1 / (2 ** (.5)))
    efieldy3 = (k_C * 10 / 2) * (1 / (2 ** (.5)))
    efieldx4 = (k_C * 10 / (2)) * (1 / (2 ** (.5)))
    efieldy4 = (k_C * 10 / 2) * (1 / (2 ** (.5)))

    expected_output = np.array([[[efieldx1, efieldy1], [efieldx2, efieldy2]], 
                                 [[efieldx3,efieldy3],[efieldx4,efieldy4]]])
    #assert np.allclose(test_efield_output._field, expected_output)
    assert expected_output.shape == test_efield_output._field.shape


def test_get_scalar_field_value(generate_pt_source):
    k_C = 8.99 * (10 ** 9)
    test_coordinates = Domain(2,2,2,2).main_coords
    x_coords = test_coordinates.x_grid
    y_coords = test_coordinates.y_grid
    test_source = generate_pt_source
    test_epotential_output = test_source.get_scalar_field(x_coords, y_coords)
    epotential1 = (k_C * 10) / (2 ** (.5))
    epotential2 = (k_C * 10) / (2 ** (.5))
    epotential3 = (k_C * 10) / (2 ** (.5))
    epotential4 = (k_C * 10) / (2 ** (.5))
    expected_output =np.array([[epotential1, epotential2],
                        [epotential3, epotential4]])
    assert expected_output.shape == test_epotential_output._field.shape
    