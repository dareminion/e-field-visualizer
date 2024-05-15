from src.math.Fields import Field

class VectorField(Field):

    '''
    Inherit Field class
    Last entry of shape has to be equal to the number of entries prior

    Ex./ shape returns (10,30,5,3), the 4th number in the tuple should
    be equal to the number of entires prior, which is 3

    More functionatilites may be added to this class 
    '''