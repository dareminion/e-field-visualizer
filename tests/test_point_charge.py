import pytest
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField
from src.physics.PointCharge import ElectrostaticPtCharge
from src.physics.ElectrostaticSource import FiducialElectrostaticSource
from src.domain.Coordinates import Coordinates
from src.domain.Domain import Domain
import numpy as np


@pytest.fixture
def generate_pt_source():
    test_placement_data = {'x': 0, 'y':0}
    test_pt_source = ElectrostaticPtCharge(10, test_placement_data)

    return test_pt_source

def test_import():
    assert True

def test_efield_return_type(generate_pt_source):
    test_coordinate = Domain(5,5,5,5).main_coords
    test_source = generate_pt_source
    output = test_source.electric_field(test_coordinate)
    assert isinstance(output, VectorField)
    assert output._field.shape == (5,5,2)
    
def test_electric_potential_return_tyoe(generate_pt_source):
    test_coordinate = Domain(5,5,5,5).main_coords
    test_source = generate_pt_source
    output = test_source.electric_potential(test_coordinate)
    assert isinstance(output, ScalarField)
    assert output._field.shape == (5,5)

    