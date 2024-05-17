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

       Error Checking method above has short comings as some of numpy's workarounds such
       as adding a single value to an array will cause this to break

       For the purposes of the current implementation of this wrapper, this will work fine
       If time permits, a higher level of error checking will be implemented
       '''
       try: 
        return self.__class__(np.add(self._field , other._field))
       except ValueError:
          return self
    

    
        