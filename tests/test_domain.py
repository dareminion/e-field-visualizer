# Testing Domain.py
import pytest
from src.domain.Domain import Domain


# Generate Sample Domain
@pytest.fixture
def generate_sample_domain():

    return Domain(7,7,7,7)

# Test imports
def test_imports():
    assert True

# Check if span of x and y values is correct:
def test_check_span(generate_sample_domain):
    
    # Generates a domain
    domain = generate_sample_domain

    intended_x_span = domain.x_span
    intended_y_span = domain.y_span

    # Obtains the grids
    x_grid = domain.main_coords.x_grid
    y_grid = domain.main_coords.y_grid

   
    assert len(x_grid) == intended_x_span
    assert len(y_grid) == intended_y_span

# Check if the grid size is correct:
def test_check_grid_size(generate_sample_domain):

    # Generates a domain
    domain = generate_sample_domain

    intended_domain_size = (7, 7)

    # Obtains the grids
    x_grid = domain.main_coords.x_grid
    y_grid = domain.main_coords.y_grid
    x_size = x_grid.shape
    y_size = y_grid.shape

    assert intended_domain_size == x_size
    assert intended_domain_size == y_size
