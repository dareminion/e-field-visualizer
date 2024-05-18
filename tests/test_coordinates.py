# Testing Coordinates.py
import numpy as np
from src.domain.Domain import Domain
from src.domain.Coordinates import Coordinates


# Generate Sample Coordinate object
def generate_sample_coordinate():

    return Domain(7,7,7,7).main_coords

# Test imports
def test_imports() -> None:
    assert True

# Tests if coordinates are translated correctly
def test_translate() -> None:

    original_coords = generate_sample_coordinate()
    translated_coords = original_coords.translate(3, 3)

    assert np.array_equal(translated_coords.x_grid , original_coords.x_grid - 3)
    assert np.array_equal(translated_coords.y_grid , original_coords.y_grid - 3)

# Tests if the simplest case of a coordinate rotation
def test_simple_rotate() -> None:
    # Define simple grids
    x_grid = np.array([[1, 0], [0, 1]])
    y_grid = np.array([[0, 1], [-1, 0]])
    coords = Coordinates(x_grid, y_grid)

    # Rotate 90 degrees (pi/2 radians)
    theta = np.pi / 2
    rotated_coords = coords.rotate(theta)

    # Define expected results after 90 degrees rotation
    expected_x_grid = np.array([[0, -1], [1, 0]])
    expected_y_grid = np.array([[1, 0], [0, 1]])

    # Assert the rotated coordinates are as expected
    np.testing.assert_array_almost_equal(rotated_coords.x_grid, expected_x_grid)
    np.testing.assert_array_almost_equal(rotated_coords.y_grid, expected_y_grid)

# Tests if all coordinates are rotated correctly (more complex)
def test_rotate() -> None:

    original_coords = generate_sample_coordinate()

    # Rotate 90 degrees (pi/2 radians)
    theta = np.pi / 2
    rotated_coords = original_coords.rotate(theta) 

    # Define expected results after 90 degrees rotation
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    original_coords_flat = np.stack((original_coords.x_grid.ravel(), original_coords.y_grid.ravel()), axis=1)
    expected_coords_flat = original_coords_flat @ rotation_matrix.T
    expected_x_grid = expected_coords_flat[:, 0].reshape(original_coords.x_grid.shape)
    expected_y_grid = expected_coords_flat[:, 1].reshape(original_coords.y_grid.shape)

    # Assert the rotated coordinates are as expected
    np.testing.assert_array_almost_equal(rotated_coords.x_grid, expected_x_grid)
    np.testing.assert_array_almost_equal(rotated_coords.y_grid, expected_y_grid)   


# # Tests return type of get_efield()
# def test_get_efield_return_type() -> None:

#     sample_domain = Domain(3, 3, 3, 3)
#     sample_coords = Domain(3, 3, 3, 3).main_coords
#     source = PlaceableSource()
#     result = sample_domain.get_efield(source, sample_coords)
#     assert isinstance(result, VectorField)

# # Tests return type of get_epotential()
# def test_get_epotential_return_type() -> None:

#     sample_domain = Domain(3, 3, 3, 3)
#     sample_coords = Domain(3, 3, 3, 3).main_coords
#     source = PlaceableSource()
#     result = sample_domain.get_epotential(source, sample_coords)
#     assert isinstance(result, ScalarField)
