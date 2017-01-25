import unittest

from vector import Vector
from plane import Plane

class TestPlane(unittest.TestCase):
    p1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
    p2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)

    p3 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
    p4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

    p5 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
    p6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)


    def test_equal(self):
        self.assertTrue(self.p1 == self.p2)
        self.assertFalse(self.p3 == self.p4)
        self.assertFalse(self.p5 == self.p6)


    def test_is_parallel(self):
        self.assertTrue(self.p1.is_parallel(self.p2))
        self.assertFalse(self.p3.is_parallel(self.p4))
        self.assertTrue(self.p5.is_parallel(self.p6))


if __name__ == '__main__':
    unittest.main()