# Testing Coordinates.py
import pytest
import numpy as np
from src.domain.Domain import Domain
from src.domain.Coordinates import Coordinates
from src.physics.placeablesource import PlaceableSource
from src.math.VectorFields import VectorField
from src.math.ScalarFields import ScalarField

# Generate Sample Coordinate object
def generate_sample_coordinate():

    return Domain(7,7,7,7).main_coords

# Test imports
def test_imports() -> None:
    assert True

# Tests if coordinates are shifted correctly
def test_shift_coordinates() -> None:

    original_coords = generate_sample_coordinate()
    shifted_coords = original_coords.shift_coordinates(3, 3)

    assert np.array_equal(shifted_coords.x_grid , original_coords.x_grid + 3)
    assert np.array_equal(shifted_coords.y_grid , original_coords.y_grid + 3)

# Tests return type of get_efield()
def test_get_efield_return_type() -> None:

    sample_domain = Domain(3, 3, 3, 3)
    sample_coords = Domain(3, 3, 3, 3).main_coords
    source = PlaceableSource()
    result = sample_domain.get_efield(source, sample_coords)
    assert isinstance(result, VectorField)

# Tests return type of get_epotential()
def test_get_epotential_return_type() -> None:

    sample_domain = Domain(3, 3, 3, 3)
    sample_coords = Domain(3, 3, 3, 3).main_coords
    source = PlaceableSource()
    result = sample_domain.get_epotential(source, sample_coords)
    assert isinstance(result, ScalarField)