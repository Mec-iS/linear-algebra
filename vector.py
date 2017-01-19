from itertools import zip_longest
from math import sqrt, acos

class Vector(object):
    def __init__(self, coordinates):
        try:
            check = all(isinstance(c, (int, float)) for c in coordinates)
            if check:
                setattr(self, 'coordinates', tuple(coordinates))
            else:
                raise ValueError('all coordinates must be int or float')  
        except TypeError as e:
            raise TypeError('coordinates must be a sequence')
        except ValueError as e:
            raise ValueError('all coordinates must be int or float')

    def __str__(self):
        return 'Vector {}'.format(str(self.coordinates))

    def __eq__(self, other):
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Vectors')
        return self.coordinates == other.coordinates
    
    def __same_class__(self, other):
        """
        Chek if two vectors are in the same class using the
         unit (normalization).
        """
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Vectors')
        return True if self.unit == other.unit else False

    def __same_class_dot_(self, other):
        """
        Chek if two vectors are in the same class using dot 
         product.
        """
        pass

    @property
    def dimension(self):
        return len(self.coordinates)
 
    def add(self, other):
        """
        Return a Vector that is the summation of the inputs.

        #TODO: implement n addends
        """
        return self.__class__(
            tuple(map(
              lambda x:x[0] + x[1], 
              zip_longest(self.coordinates,other.coordinates, fillvalue=0)
              )
            )
        )

    def subtract(self, other):
        """
        Return a Vector that is the subtraction of the first
         input and the second.
        """
        return self.__class__(
            tuple(map(
              lambda x:x[0] - x[1], 
              zip_longest(self.coordinates,other.coordinates, fillvalue=0)
              )
            )
        )

    def multiply(self, scalar):
        """
        Return a Vector that is the scalar multiplication of the
         origianl vector and the scalar.
        """
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
        """
        Return the scalar that represent the Magnitude of the
         original vector: ||v||
        """
        if all(c == 0 for c in self.coordinates): return None
        
        return sqrt(
          sum(
            tuple(map(
              lambda x:x * x, 
              self.coordinates
            )
          ))
        )

    @property
    def unit(self):
        """
        Return a vector that is the Unit of the original vector:
         |u| = |v| * (1 / ||v||) 
        """
        return self.__class__(
          tuple([
            c * (1 / self.magnitude)
            for c in self.coordinates
          ])  
        )

    def dot(self, other):
        """
        Return the Dot Product of two vectors.

        Definition:
          |v| dot |w| = ||v|| dot ||w|| * cos(teta)
        Operation:
          |v| dot |w| = v1*w1 + v2*w2 + ... = vn*wn
        """
        return sum(
          tuple(map(
            lambda x:x[0] * x[1], 
            zip_longest(self.coordinates, other.coordinates, fillvalue=0)
            )
          )
        )

    def angle(self, other):
        """
        Return the asangle teta between two vectors using the Dot
         Product operation.

        Definition:
         |v| dot |w| = ||v|| * ||w|| * cos(teta)
        Operation:
         angle = arccos(|v| dot |w| / (||v|| * ||w||))
        """
        if other.__class__ != self.__class__:
            raise TypeError('can angle only two Vectors')
        return acos(self.dot(other) / (self.magnitude * other.magnitude))


