import abc

class PlaceableSource(abc.ABC):

    placement_data = None
    transformed_grid = None

    def __init__(self, fiedsource, gridtransformer):
        self.fieldsource = fieldsource
        self._gridtransformer = gridtransformer

    
    def _gridtransform(self, grid):
        if not self._transformed_grid:
            self._transformed_grid = self._gridtransformer(g,self.placement_data)
            return self._transfromed_grid


    def place(self, placement_data: dict):
        self.placement_data = placement_data
        self._transformed_grid = None

    def get_vector_field(grid):
        tgrid = self._gridtransform(grid)
        return self.fieldsource.get_vector_field(tgrid)

    def get_scalar_field(grid):
        tgrid = self._gridtransform(grid)
        return self.fieldsource.get_scalar_field(self._transformed_grid)

    