# Testing Grid.py
import pytest
import numpy as np
from src.grid.Grid import Grid

# Generate Sample Grid
def generate_sample_grid(x_span, y_span, num_x_coords, num_y_coords):

    return Grid(7,7,7,7)

# Test imports
def test_imports():
    assert True

# Check if span of x and y values is correct:
def test_check_span():
    
    # Generates a grid
    grid = generate_sample_grid(7, 7, 7, 7)

    intended_x_span = grid.x_span
    intended_y_span = grid.y_span

    # Unpacks the tuple of grids returned by make_grid()
    x_grid, y_grid = grid.make_grid()
   
    assert len(x_grid) == intended_x_span
    assert len(y_grid) == intended_y_span

# Check if the grid size is correct:
def test_check_grid_size():

    # Generates a grid
    grid = generate_sample_grid(7, 7, 7, 7)

    intended_grid_size = (7, 7)

    # Unpacks the tuple of grids returned by make_grid()
    x_grid, y_grid = grid.make_grid()
    x_size = x_grid.shape
    y_size = y_grid.shape

    assert intended_grid_size == x_size
    assert intended_grid_size == y_size
