import unittest

from vector import Vector
from line import Line2D

class TestLine(unittest.TestCase):

    def test_init(self):
        l1 = Line2D(Vector([4.046, 2.836]), 1.21)
        l2 = Line2D(Vector([10.115, 7.09]), 3.025)

        self.assertTrue(l1.A == 4.046 and l1.B ==  2.836 and l1.k == 1.21)
        self.assertTrue(l2.A == 10.115 and l2.B ==  7.09 and l2.k == 3.025)

    def test_intersection(self):
        l1 = Line2D(Vector([4.046, 2.836]), 1.21)
        l2 = Line2D(Vector([10.115, 7.09]), 3.025)
        self.assertRaises(ValueError, l1.intersection, l2)

        l3 = Line2D(Vector([7.204, 3.182]), 8.68)
        l4 = Line2D(Vector([8.172, 4.114]), 9.883)
        self.assertTrue(l3.intersection(l4) == (1.1727766354646403, 0.07269551166333513))

        l5 = Line2D(Vector([1.182, 5.562]), 6.744)
        l6 = Line2D(Vector([1.773, 8.343]), 9.525)
        self.assertRaises(ValueError, l5.intersection, l6)





if __name__ == '__main__':
    unittest.main()