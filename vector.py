from itertools import zip_longest
from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        self.coordinates, self.dimensions = None, None
        try:
            check = all(isinstance(c, (int, float)) for c in coordinates)
            if check:
                self.coordinates = tuple(coordinates)
            else:
                raise ValueError('all coordinates must be int or float')  
        except TypeError as e:
            raise TypeError('coordinates must be a sequence')
        except ValueError as e:
            raise ValueError('all coordinates must be int or float')

        self.dimension = len(self.coordinates)

    def __str__(self):
        return 'Vector {}'.format(str(self.coordinates))

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Vectors')
        return self.coordinates == other.coordinates
    
    def __same_class__(self, other):
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Vectors')
        return True if self.unit == other.unit else False

    """@property
    def coordinates(self):
        return self.coordinates

    @property
    def dimension(self):
        return self.dimension"""
 
    def add(self, other):
        return self.__class__(
            tuple(map(
              lambda x:x[0] + x[1], 
              zip_longest(self.coordinates,other.coordinates, fillvalue=0)
              )
            )
        )

    def subtract(self, other):
        return self.__class__(
            tuple(map(
              lambda x:x[0] - x[1], 
              zip_longest(self.coordinates,other.coordinates, fillvalue=0)
              )
            )
        )

    def multiply(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError('scalar must be an integer or float')
        return self.__class__(
            tuple(map(
              lambda x:x * scalar, 
              self.coordinates
            )
        ))

    @property
    def magnitude(self):
        if all(c == 0 for c in self.coordinates): return None
        
        return sqrt(
            sum(
                tuple(
                    map(
                        lambda x:x * x, 
                        self.coordinates
                    )
                )
            )
        )

    @property
    def unit(self):
        return self.__class__(
            tuple([
              c * (1 / self.magnitude)
              for c in self.coordinates
            ])  
        )


