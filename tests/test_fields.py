import numpy as np
from src.math.ScalarFields import ScalarField
from src.math.VectorFields import VectorField


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

def test_VectorField_Wrapper_Test():
    Expected_Array = np.zeros((120,230,2))
    Vector_Numpy_Array = np.zeros((120,230,2))
    test_vector_field = VectorField(Vector_Numpy_Array)
    assert test_vector_field._field.all() == Expected_Array.all()

def test_Scalar_Addition():
    Expected_Array = np.full((2,2), 10)
    Scalar_Numpy_Array_1 = np.full((2,2), 4)
    Scalar_Numpy_Array_2 = np.full((2,2), 6)
    test_scalar_field_1 = ScalarField(Scalar_Numpy_Array_1)
    test_scalar_field_2 = ScalarField(Scalar_Numpy_Array_2)
    assert np.array_equal(Expected_Array, (test_scalar_field_1 + test_scalar_field_2)._field)

def test_Scalar_Addition_Error_Case():
    Expected_Array = np.full((25,25), 4)
    Scalar_Numpy_Array_1 = np.full((25,25), 4)
    Scalar_Numpy_Array_2 = np.full((5,5), 6)
    test_scalar_field_1 = ScalarField(Scalar_Numpy_Array_1)
    test_scalar_field_2 = ScalarField(Scalar_Numpy_Array_2)
    assert np.array_equal(Expected_Array, (test_scalar_field_1 + test_scalar_field_2)._field)

def test_Vector_Addition():
    Expected_Array = np.full((20,30,2),(100,50))
    Vector_Numpy_Array_1 = np.full((20,30,2),(73,19))
    Vector_Numpy_Array_2 = np.full((20,30,2),(27,31))
    test_vfield1 = VectorField(Vector_Numpy_Array_1)
    test_vfield2 = VectorField(Vector_Numpy_Array_2)
    assert np.array_equal(Expected_Array, (test_vfield1 + test_vfield2)._field)

def test_Vector_Addition_Error_Case():
    Expected_Array = np.full((2,3,2),(73,19))
    Vector_Numpy_Array_1 = np.full((2,3,2),(73,19))
    Vector_Numpy_Array_2 = np.full((2,3,4,3),(27,31,10))
    test_vfield1 = VectorField(Vector_Numpy_Array_1)
    test_vfield2 = VectorField(Vector_Numpy_Array_2)
    assert np.array_equal(Expected_Array, (test_vfield1 + test_vfield2)._field)