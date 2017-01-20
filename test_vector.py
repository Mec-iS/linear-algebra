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
        self.assertTrue(w.magnitude == 14.053007686)

        y = w.multiply(2.4565737456)
        self.assertTrue(y.magnitude == 34.52224973)

    def test_addition(self):
        w = Vector(self.test)
        y = Vector(self.test).add(Vector([1, 2, 3]))

        self.assertTrue(w.add(y) == Vector([12.0926914, 15.470691199999997, 8.471526912, 8.69126914, 19.4926912]))

        w = Vector(self.test).multiply(2.13)
        y = Vector(self.test)

        self.assertTrue(w.add(y) == Vector([17.360062041, 21.081631727999998, 8.56293961728, 13.601836204099998, 30.506061728]))



if __name__ == '__main__':
    unittest.main()