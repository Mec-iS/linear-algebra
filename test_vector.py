import unittest

from vector import Vector

class TestVector(unittest.TestCase):

    test = [5.5463457,6.7353456,2.735763456,4.34563457,9.7463456]

    def test_init(self):
        
        w = Vector([5.5463457,6.7353456,2.735763456,4.34563457,9.7463456])
        [
          self.assertTrue(c == self.test[i]) 
          for i, c in enumerate(w.coordinates)
        ]

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


if __name__ == '__main__':
    unittest.main()