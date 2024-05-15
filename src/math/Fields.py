import abc
import numpy as np

class Fields(abc.ABC):

    ''' Abstract Base Class describing Fields Interface
    '''

    @abc.abstractmethod
    def __add__(self, other) -> np.ndarray:
        '''
        __add__ Method for fields

        Requires a checking step before addition that is more than just class checking
        Size of field is also required
        '''
        pass
        
        