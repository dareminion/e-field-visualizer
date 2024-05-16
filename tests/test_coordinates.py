# Testing Coordinates.py
import pytest
import numpy as np
from src.domain.Domain import Domain
from src.domain.Coordinates import Coordinates

# Generate Sample Coordinate object
def generate_sample_coordinate():

    return Domain(7,7,7,7).main_coords

# Test imports
def test_imports() -> None:
    assert True

def test_shift_coordinates() -> None:

    original_coords = generate_sample_coordinate()
    shifted_coords = original_coords.shift_coordinates(3, 3)

    assert np.array_equal(shifted_coords.x_grid , original_coords.x_grid + 3)
    assert np.array_equal(shifted_coords.y_grid , original_coords.y_grid + 3)
