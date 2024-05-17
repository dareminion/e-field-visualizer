'''
Once class files are created and PR'd into main repo, more imports will be defined
'''

import pytest
import numpy as np
from src.math.VectorFields import VectorField
from src.factories.PointSourceFactory import PointSourceFactory
from src.physics.PlaceableSource import PlaceableSource
from src.domain.Domain import Domain



'''
test_workflows is just a temporary test for the workflows test to pass when a PR occurs
'''
def test_workflows():
    assert True

def test_FactorytoVectorField():
    domain = Domain(10, 10, 10, 10)

    placement_data = {'x' : 2,
            'y' : 3}

    factory = PointSourceFactory()

    source = factory.create_placeable_source(10)

    source.place(placement_data)

    vector_field = source.get_vector_field(domain.main_coords)

    assert isinstance(vector_field, VectorField)

'''
Small Integration Tests will be here after class creatio is complete
'''