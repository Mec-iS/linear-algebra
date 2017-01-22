from vector import Vector

class Line2D(object):
    """
    Parametrization of a line.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Definition:
     Ax = By = k
    Operation:
     find a basepoint and a direction vector to define a line
    """
    __ROUNDING = 9

    def __init__(self, normal_vector=None, const_term=None):
        # normal vector = [A, B]
        self.normal_vector = normal_vector if normal_vector is not None else ValueError('line needs a normal vector')
        if not self.normal_vector.__class__ == Vector: raise TypeError('normal vector must be a Vector')
        self.term = self.k = const_term if const_term is not None else 0

        self.A = self.normal_vector.coordinates[0]
        self.B = self.normal_vector.coordinates[1]

    def set_basepoint(self, rounding=__ROUNDING):
        if self.normal_vector.coordinates[1] != 0:
            # B != 0 so (0, k/B) is a base point
            return round(self.term / self.normal_vector.coordinates[1], rounding)
        if self.normal_vector.coordinates[0] != 0:
            # A != 0 so (k/A, 0) is a base point
            return round(self.term / self.normal_vector.coordinates[1], rounding)

    def __eq__(self, other):
        """
        Two lines are the same line if a vector created by picking two random 
         points from both is orthogonal to the normal vector. 
        """
        if not self.is_parallel(other):
            return False
        test_vector = Vector([self.basepoint, other.basepoint])
        return test_vector.is_orthogonal(self.normal_vector)

    def is_parallel(self, other):
        """
        Two lines are parallel if their normal vectors are parallel.
        """
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Lines')
        return self.normal_vector.is_parallel(other.normal_vector)

    @property
    def normal(self):
        return self.normal_vector

    @property
    def constant(self):
        return self.term

    @property
    def basepoint(self):
        return self.set_basepoint()

    def intersection(self, other, rounding=__ROUNDING):
        """
        Find intersection of two lines that are not parallel nor the same line
        """
        if other.__class__ != self.__class__:
            raise TypeError('can compare only two Lines')
        if self == other:
            raise ValueError('Lines have infinite points in common')
        if self.is_parallel(other):
            raise ValueError('Lines are parallel')
       
        denominator = round((self.A * other.B) - (self.B * other.A), rounding)

        numerator1 = round((other.B * self.k) - (self.B * other.k), rounding)
        numerator2 = round(-(other.A * self.k) +  (self.A * other.k), rounding)
        
        return numerator1 / denominator, numerator2 / denominator


