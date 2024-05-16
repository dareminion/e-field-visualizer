import abc
import numpy as np

class Field(abc.ABC):

    ''' Abstract Base Class describing Fields Interface
    '''

    def __init__(self, field : np.ndarray) -> None:
        
        '''
        For interal functions to call the numpy array version of the field
        for math purposes such as __add__.
        '''
        self._field = field


    def __add__(self, other) -> 'Field':

       ''' 
       Using numpy's .add function on the two numpy versions of a field that returns
       the class of field
       
       Error Checking:
       If the shapes of the two fields are not the same, numpy raises a value error
       When value error is raised, the original field is returned
       '''
       try: 
        return self.__class__(np.add(self._field , other._field))
       except ValueError:
          return self
    

    
        