# Testing Domain.py
import pytest
import numpy as np
from src.domain.Domain import Domain
from src.domain.Coordinates import Coordinates

# Generate Sample Grid
def generate_sample_domain(x_span, y_span, num_x_coords, num_y_coords):

    return Domain(7,7,7,7)

# Test imports
def test_imports():
    assert True

# Check if span of x and y values is correct:
def test_check_span():
    
    # Generates a domain
    domain = generate_sample_domain(7, 7, 7, 7)

    intended_x_span = domain.x_span
    intended_y_span = domain.y_span

    # Obtains the grids
    x_grid = domain.main_coords.x_grid
    y_grid = domain.main_coords.y_grid

   
    assert len(x_grid) == intended_x_span
    assert len(y_grid) == intended_y_span

# Check if the grid size is correct:
def test_check_grid_size():

    # Generates a domain
    domain = generate_sample_domain(7, 7, 7, 7)

    intended_domain_size = (7, 7)

    # Obtains the grids
    x_grid = domain.main_coords.x_grid
    y_grid = domain.main_coords.y_grid
    x_size = x_grid.shape
    y_size = y_grid.shape

    assert intended_domain_size == x_size
    assert intended_domain_size == y_size
