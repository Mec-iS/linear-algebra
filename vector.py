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


v = Vector([1,2,3,7,9])
w = Vector([5,6,2,4,9,1,4,8,4])

print(v.__class__)

n = Vector([0,0,0,0,0,0])
#print(n.magnitude)

v_ = v.multiply(3.5)

print(v.add(w))
print(v.subtract(w))
print(w.subtract(v))
print(v.multiply(3))
print(v == w)
print(v.magnitude)
print(w.magnitude)
print(v.unit)
print(w.unit)
print(v.__same_class__(w))
print(v.__same_class__(v_))
