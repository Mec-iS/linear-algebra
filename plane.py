from vector import Vector

class Plane(object):
    """
    Class of planes in a 3D space.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    __ROUNDING = 9

    def __init__(self, normal_vector=None, const_term=None):
        # normal vector = [A, B, C]
        # direction vector = [x, y, z]
        if not normal_vector.__class__ == Vector: raise TypeError('normal vector must be of class Vector')
        
        if normal_vector is not None and normal_vector.dimension == 3:
            self.normal_vector = normal_vector
        else: raise ValueError('plane needs a normal vector')
        self.term = self.k = const_term if const_term is not None else 0

        self.A = self.normal_vector.coordinates[0]
        self.B = self.normal_vector.coordinates[1]
        self.C = self.normal_vector.coordinates[2]

    def __str__(self):
        return str('Plane with normal {} and constant {}').format(str(self.normal), str(self.term))

    def __eq__(self, other):
        """
        Two planes are the same plane if a vector created by picking two random 
         points from both is orthogonal to the normal vector. 
        """
        if not self.is_parallel(other):
            return False
        test_vector = Vector([
            self.basepoint.X - other.basepoint.X, 
            self.basepoint.Y - other.basepoint.Y,
            self.basepoint.Z - other.basepoint.Z
        ])
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
            raise TypeError('can compare only two Planes')
        return self.normal_vector.is_parallel(other.normal_vector)

    @property
    def normal(self):
        return self.normal_vector

    @property
    def dimension(self):
        return len(self.normal_vector)

    @property
    def constant(self):
        return self.term

    @property
    def basepoint(self):
        return self.set_basepoint()

    def set_basepoint(self, rounding=__ROUNDING):
        n = self.normal.coordinates
        base = [0] * self.dimension
        i = self.first_nonzero_index(n)
        base[i] = round(self.term / n[i], rounding)
        return Vector(base)

    @staticmethod
    def first_nonzero_index(iterable):
        from math import isclose
        for k, item in enumerate(iterable):
            if not isclose(item, 0):
                return k
        #raise ValueError('normal vector cannot be zero vector')

    def intersection(self, other):
        """
        The intersection of two planes is equal to the cross product of their normal 
         vectors.
        """
        if self.normal.is_parallel(other.normal):
            raise ValueError('Planes are parallel, they don\'t have common points')

        return self.normal.cross_product(other)

