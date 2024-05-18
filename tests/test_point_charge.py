import pytest
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField
from src.physics.PointCharge import PointCharge
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
from src.domain.Coordinates import Coordinates
from src.domain.Domain import Domain
import numpy as np
import scipy.constants as const

k_C = 1 / (4 * const.pi * const.epsilon_0)

@pytest.fixture
def generate_pt_source():
    test_point_charge = PointCharge(10)

    return (test_point_charge)

def test_import():
    assert True

def test_efield_return_type(generate_pt_source):
    test_x, test_y = 2, 5
    test_source = generate_pt_source
    output = test_source.efield(test_x, test_y)
    assert isinstance(output, np.ndarray)
    assert output.shape == (2,)
    
def test_electric_potential_return_type(generate_pt_source):
    test_x, test_y = 2, 5
    test_source = generate_pt_source
    output = test_source.epotential(test_x, test_y)
    assert isinstance(output, float)

def test_efield_value(generate_pt_source):
    test_x, test_y = 2, 5
    test_source = generate_pt_source
    test_efield_output = test_source.efield(test_x,test_y)
    expected_x_output = ((k_C * 10 ) / (29)) * (2/(29 ** .5)) 
    expected_y_output = ((( (k_C)) * 10 ) / (29)) * (5/(29 ** .5))
    expected_output = np.array([expected_x_output, expected_y_output])
    assert np.allclose(test_efield_output,expected_output)

def test_epotential_value(generate_pt_source):
    test_x, test_y = 2, 5
    test_source = generate_pt_source
    test_epotential_output = test_source.epotential(test_x,test_y)
    expected_output = (k_C * 10) / (29 ** .5)
    assert test_epotential_output == expected_output