import abc
import numpy as np

class field(abc.ABC):

    ''' Abstract Base Class describing Fields Interface
    '''

    @abc.abstractmethod
    def __add__(self, other) -> field:
        '''
        __add__ Method for fields

        Requires a checking step before addition that is more than just class checking
        Size of field is also required
        '''
        pass

    @abc.abstractmethod
    def shape(self) -> tuple:
        '''
        Inherit from numpy's arr.shape function
        '''
        
        