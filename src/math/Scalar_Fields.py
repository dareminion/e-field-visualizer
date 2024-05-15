import numpy as np
from src.math.Fields import field

class scalar_field(field):

    def __add__(self, other) -> scalar_field:
        
        # Check field_size logic
        shape1 = self.shape
        shape2 = self.shape

        # If field sizes are the same, add the values using np.add

        if shape1 == shape2
            return np.add(self,other)