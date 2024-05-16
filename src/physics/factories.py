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