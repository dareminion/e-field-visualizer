from src.math.Fields import Field
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField
import numpy as np
import pytest


def test_import():
    assert True

def test_ScalarField_Typechecking():
    Scalar_Numpy_Array = np.ones((3,4))
    test_scalar_field = ScalarField(Scalar_Numpy_Array)
    assert isinstance(test_scalar_field, ScalarField)

def test_ScalarField_Wrapper_Test():
    Expected_Array = np.zeros((13,49))
    Scalar_Numpy_Array = np.zeros((13,49))
    test_scalar_field = ScalarField(Scalar_Numpy_Array)
    assert test_scalar_field._field.all() == Expected_Array.all()

def test_VectorField_Typechecking():
    Vector_Numpy_Array = np.zeros((100,100,2))
    test_vector_field = VectorField(Vector_Numpy_Array)
    assert isinstance(test_vector_field, VectorField)