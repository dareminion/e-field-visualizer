from src.domain.Domain import Domain
from src.math.VectorFields import VectorField
from src.visuals.Visualizer import Visualizer
from src.factories.PointSourceFactory import PointSourceFactory

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

def test_full_run():
    def partial_demo():
        demo_domain = Domain(100, 100, 50, 50)

        placement_data = {'x': -10, 'y': 20}

        factory = PointSourceFactory()

        source = factory.create_placeable_source(10)
        
        source.place(placement_data)

        demo_domain.add_a_source(source, 'source 1')

        vector_field = demo_domain.get_efield(source, demo_domain.main_coords)
        
        scalar_field = demo_domain.get_epotential(source, demo_domain.main_coords)

        visualizer = Visualizer(demo_domain)
        
        visualizer.place_source(source)

        visualizer.plot_scalar_field(scalar_field._field, 'heatmap')
        
        visualizer.plot_vector_field(vector_field._field, 'quiver')

        return 0
    if partial_demo() == 0:
        assert True
