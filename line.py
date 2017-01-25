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
        self.normal_vector = normal_vector \
            if normal_vector is not None and not normal_vector.is_zero_vector \
            else ValueError('line needs a normal vector and must be not a zero vector')
        if not self.normal_vector.__class__ == Vector: raise TypeError('normal vector must be of class Vector')
        self.term = self.k = const_term if const_term is not None else 0

        self.A = self.normal_vector.coordinates[0]
        self.B = self.normal_vector.coordinates[1]

    def __str__(self):
        return str('Line with normal {} and basepoint ({})').format(str(self.normal), str(self.basepoint))

    def __eq__(self, other):
        """
        Two lines are the same line if a vector created by picking two random 
         points from both is orthogonal to the normal vector. 
        """
        if not self.is_parallel(other):
            return False
        test_vector = Vector([self.basepoint, other.basepoint])
        return test_vector.is_orthogonal(self.normal_vector)

    def __ne__(self, other):
        """
        Two lines are not the same line. 
        """
        return not self.__eq__(other)

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

    def set_basepoint(self, rounding=__ROUNDING):
        if self.B != 0:
            # B != 0 so (0, k/B) is a base point
            return round(self.term / self.B, rounding)
        if self.A != 0:
            # A != 0 so (k/A, 0) is a base point
            return round(self.term / self.A, rounding)

        raise ValueError('normal vector cannot be the zero vector')

    @property
    def direction(self, rounding=__ROUNDING):
        return Vector([self.B, -self.A])

    def intersection(self, other, rounding=__ROUNDING):
        """
        Find intersection of more than two lines that are not parallel nor the same line.
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

    def intersection_multi(self, other, rounding=__ROUNDING):
        """
        Find all the intersections of two or more lines that are not parallel nor the same line.
         `other` is a list.
        """
        if not isinstance(other, list):
            other = [other]
        if not all(o.__class__ == self.__class__ for o in other):
            raise TypeError('can compare only Lines')
               
        full = [self] + other
        import itertools
        prod = []
        [prod.append(f) 
          for f in itertools.product(full, full) 
          if f[0] is not f[1] and (f[1], f[0]) not in prod]

        if any(p[0] == p[1] or p[0].is_parallel(p[1]) for p in prod): 
            raise ValueError('two of the lines are the same line or they are parallel')

        return [o[0].intersection(o[1]) for o in prod]
            



