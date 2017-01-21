import unittest

from vector import Vector

class TestVector(unittest.TestCase):

    test = [5.5463457,6.7353456,2.735763456,4.34563457,9.7463456]
    dim = len(test)

    def test_init(self):
        
        w = Vector([5.5463457,6.7353456,2.735763456,4.34563457,9.7463456])
        [
          self.assertTrue(c == self.test[i]) 
          for i, c in enumerate(w.coordinates)
        ]

    def test_multiply(self):
        w = Vector(self.test)
        v = w.multiply(1.3463745645)

        r = Vector(list(map(
              lambda x:x * 1.3463745645, 
              w.coordinates
            )
        ))
        self.assertTrue(r == v)

    def test_unit(self):
        w = Vector(self.test)
        v = w.multiply(3.7567)

        self.assertTrue(w.unit == v.unit)

    def test__same_class(self):
        w = Vector(self.test)
        v = w.multiply(3.7567)

        self.assertTrue(w.__same_class__(v))

    def test__same_class_dot(self):
        w = Vector(self.test)
        v = w.multiply(3.2314124347)

        self.assertTrue(w.__same_class_dot__(v))

    def test_is_zero(self):
        z = Vector([0, 0, 0, 0, 0])
        self.assertTrue(z.is_zero_vector)

        y = Vector([0.00000000000001, 0, 0, 0, 0])
        self.assertTrue(y.is_zero_vector)

        k = Vector([0.0001, 0, 0, 0, 0])
        self.assertFalse(k.is_zero_vector)

    def test_dimension(self):
        w = Vector(self.test)
        self.assertTrue(w.dimension == self.dim)

        y = Vector(self.test + [1, 2, 3])
        self.assertTrue(y.dimension == self.dim + 3)

    def test_magnitude(self):
        w = Vector(self.test)
        self.assertTrue(w.magnitude == 14.053007686369)

        y = w.multiply(2.4565737456)
        self.assertTrue(y.magnitude == 34.522249729049)

    def test_addition(self):
        w = Vector(self.test)
        y = Vector(self.test).add(Vector([1, 2, 3]))

        self.assertTrue(w.add(y) == Vector([12.0926914, 15.470691199999997, 8.471526912, 8.69126914, 19.4926912]))

        w = Vector(self.test).multiply(2.13)
        y = Vector(self.test)

        self.assertTrue(w.add(y) == Vector([17.360062041, 21.081631727999998, 8.56293961728, 13.601836204099998, 30.506061728]))

    def test_cross_product(self):
        v = Vector([5, 3, -2])
        w = Vector([-1, 0, 3])

        self.assertTrue(v.cross_product(w) == Vector([9, -13, 3]))

        y = Vector([5.4534, 3.234, -2.1])
        z = Vector([-1.98, 0, 3.8])
        self.assertTrue(y.cross_product(z) == Vector([12.2892, -16.56492, 6.40332]))

        a = Vector([2.4342, 3.2523, -2.1233])
        b = Vector([-1.9888, 0, 3.899])
        self.assertTrue(a.cross_product(b) == Vector([12.6807177, -5.26812676, 6.46817424]))


if __name__ == '__main__':
    unittest.main()