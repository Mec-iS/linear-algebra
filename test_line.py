import unittest

from vector import Vector
from line import Line2D

class TestLine(unittest.TestCase):

    l1 = Line2D(Vector([4.046, 2.836]), 1.21)
    l2 = Line2D(Vector([10.115, 7.09]), 3.025) # 
    l3 = Line2D(Vector([7.204, 3.182]), 8.68)
    l4 = Line2D(Vector([8.172, 4.114]), 9.883)
    l5 = Line2D(Vector([1.182, 5.562]), 6.744)
    l6 = Line2D(Vector([1.773, 8.343]), 9.525)
    l7 = Line2D(Vector([8.172, 4.114]), 7)  # parallel to l4

    def test_init(self):
        self.assertTrue(self.l1.A == 4.046 and self.l1.B ==  2.836 and self.l1.k == 1.21)
        self.assertTrue(self.l2.A == 10.115 and self.l2.B ==  7.09 and self.l2.k == 3.025)

    def test_is_parallel(self):
        self.assertTrue(self.l1.is_parallel(self.l2))

    def test_normal_is_orthogonal(self):
        l = Line2D(Vector([2.836, -4.046]), 1.21)
        self.assertTrue(self.l1.normal.is_orthogonal(l.normal))


    def test_intersection(self):
        #print(self.l1.intersection(self.l2))
        self.assertRaises(ValueError, self.l1.intersection, self.l2)

        self.assertTrue(self.l3.intersection(self.l4) == (1.1727766354646403, 0.07269551166333513))

        self.assertRaises(ValueError, self.l5.intersection, self.l6)

    def test_intersection_multi(self):
        self.assertTrue(self.l3.intersection_multi([self.l4]) == [(1.1727766354646403, 0.07269551166333513)])

        self.assertTrue(len(self.l3.intersection_multi([self.l4, self.l5])) == 3)

        self.assertRaises(ValueError, self.l3.intersection_multi, [self.l4, self.l7])






if __name__ == '__main__':
    unittest.main()