class PlaceableSourceFactory():
    @staticmethod
    def create_field_source():
        pass

    #another method here
    @abstractmethod
    def create_grid_transformer():
        pass

    @abstractmethod
    @staticmethod
    def create():
        field_source = self.create_field_source()
        grid_transfromer = self.create_grid_transformer()
        return PlacealbeSource(field_source, gird_transformer)

class PtSourcePlaceableFactory(PlaceableSourceFactory):
    @staticmethod
    def make_field_source(q = None):
        return PointSource(q)


    @staticmethod
    def make_grid_transfromer():
        shifter = gridtransforms.gridshift
        def gtransfroms(g placement_data):
            shift_data = placement_data['shift']
            return shifter(g, shift_data)
        return gtransforms