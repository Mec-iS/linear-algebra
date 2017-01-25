import unittest

from vector import Vector
from plane import Plane
from system import LinearSystem

class TestSystem(unittest.TestCase):
    p0 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
    p1 = Plane(normal_vector=Vector([0, 1, 0]), const_term=2)
    p2 = Plane(normal_vector=Vector([1, 1, -1]), const_term=3)
    p3 = Plane(normal_vector=Vector([1, 0, -2]), const_term=2)

    def test_init(self):
        s = LinearSystem([self.p0,self.p1,self.p2,self.p3])

        self.assertTrue(s.indices_of_first_nonzero_terms_in_each_row() == [0, 1, 0, 0])

        print('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
        print(len(s))
        print(s)

        s[0] = self.p1
        print(s)

    def test_rows_swapping_and_multiplications(self):
        s = LinearSystem([self.p0,self.p1,self.p2,self.p3])
        s.swap_rows(0,1)
        self.assertTrue(s[0] == self.p1 and s[1] == self.p0 and s[2] == self.p2 and s[3] == self.p3)

        s.swap_rows(1,3)
        self.assertTrue(s[0] == self.p1 and s[1] == self.p3 and s[2] == self.p2 and s[3] == self.p0)

        s.swap_rows(3,1)
        self.assertTrue(s[0] == self.p1 and s[1] == self.p0 and s[2] == self.p2 and s[3] == self.p3)
        
        s.multiply_coefficient_and_row(1,0)
        self.assertTrue(s[0] == self.p1 and s[1] == self.p0 and s[2] == self.p2 and s[3] == self.p3)

        s.multiply_coefficient_and_row(-1,2)
        self.assertTrue(s[0] == self.p1 and
                s[1] == self.p0 and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), const_term=-3) and
                s[3] == self.p3)

        s.multiply_coefficient_and_row(10,1)
        self.assertTrue(s[0] == self.p1 and
                s[1] == Plane(normal_vector=Vector([10, 10, 10]), const_term=10) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), const_term=-3) and
                s[3] == self.p3)

        s.add_multiple_times_row_to_row(0,0,1)
        self.assertTrue(s[0] == self.p1 and
                s[1] == Plane(normal_vector=Vector([10, 10, 10]), const_term=10) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), const_term=-3) and
                s[3] == self.p3)

        s.add_multiple_times_row_to_row(1,0,1)
        self.assertTrue(s[0] == self.p1 and
                s[1] == Plane(normal_vector=Vector([10, 11, 10]), const_term=12) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), const_term=-3) and
                s[3] == self.p3)

        s.add_multiple_times_row_to_row(-1,1,0)
        self.assertTrue(s[0] == Plane(normal_vector=Vector([-10, -10, -10]), const_term=-10) and
                s[1] == Plane(normal_vector=Vector([10, 11, 10]), const_term=12) and
                s[2] == Plane(normal_vector=Vector([-1, -1, 1]), const_term=-3) and
                s[3] == self.p3)

    def test_triangular_form(self):
        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([0, 1, 1]), const_term=2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1 and
                t[1] == p2)

        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([1, 1, 1]), const_term=2)
        s = LinearSystem([p1,p2])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1)
        #self.assertRaises(ValueError, Plane, Vector([0, 0, 0]), const_term=1)

        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([0, 1, 0]), const_term=2)
        p3 = Plane(normal_vector=Vector([1, 1, -1]), const_term=3)
        p4 = Plane(normal_vector=Vector([1, 0, -2]), const_term=2)
        s = LinearSystem([p1,p2,p3,p4])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == p1 and
                t[1] == p2 and
                t[2] == Plane(normal_vector=Vector([0, 0, -2]), const_term=2) #and
                #t[3] == Plane(Vector([0, 0, 0]), 0)
        )

        p1 = Plane(normal_vector=Vector([0, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([1, -1, 1]), const_term=2)
        p3 = Plane(normal_vector=Vector([1, 2, -5]), const_term=3)
        s = LinearSystem([p1,p2,p3])
        t = s.compute_triangular_form()
        self.assertTrue(t[0] == Plane(normal_vector=Vector([1, -1, 1]), const_term=2) and
                t[1] == Plane(normal_vector=Vector([0, 1, 1]), const_term=1) and
                t[2] == Plane(normal_vector=Vector([0, 0, -9]), const_term=-2))


    def test_reduced_row_echelon(self):
        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([0, 1, 1]), const_term=2)
        s = LinearSystem([p1,p2])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(normal_vector=Vector([1, 0, 0]), const_term=-1) and
                r[1] == p2)

        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([1, 1, 1]), const_term=2)
        s = LinearSystem([p1,p2])
        r = s.compute_rref()
        self.assertTrue(r[0] == p1) # and
                #r[1] == Plane(const_term='1'))

        p1 = Plane(normal_vector=Vector([1, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([0, 1, 0]), const_term=2)
        p3 = Plane(normal_vector=Vector([1, 1, -1]), const_term=3)
        p4 = Plane(normal_vector=Vector([1, 0, -2]), const_term=2)
        s = LinearSystem([p1,p2,p3,p4])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(normal_vector=Vector([1, 0, 0]), const_term=0) and
                r[1] == p2 and
                r[2] == Plane(normal_vector=Vector([0, 0, -2]), const_term=2) # and
                # r[3] == Plane())
            )

        p1 = Plane(normal_vector=Vector([0, 1, 1]), const_term=1)
        p2 = Plane(normal_vector=Vector([1, -1, 1]), const_term=2)
        p3 = Plane(normal_vector=Vector([1, 2, -5]), const_term=3)
        s = LinearSystem([p1,p2,p3])
        r = s.compute_rref()
        self.assertTrue(r[0] == Plane(normal_vector=Vector([1, 0, 0]), const_term=23 / 9) and
                r[1] == Plane(normal_vector=Vector([0, 1, 0]), const_term=7 / 9) and
                r[2] == Plane(normal_vector=Vector([0, 0, 1]), const_term=2 / 9)
            )

    def test_compute_gaussian(self):
        p1 = Plane(Vector([5.862, 1.178, -10.366]), -8.15)
        p2 = Plane(Vector([-2.931, -0.589, 5.183]), -4.075)

        l1 = LinearSystem([p1, p2])
        result = l1.compute_gaussian_elimination
        self.assertRaises(Exception, result)

        p3 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
        p4 = Plane(Vector([4.315, 11.132, -5.27]), 6.775)
        p5 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)

        l1 = LinearSystem([p3, p4, p5])
        print('GE 2', l1.compute_gaussian_elimination())

        p6 = Plane(Vector([5.262, 2.739, -9.878]), -3.441)
        p7 = Plane(Vector([5.111, 6.358, -7.638]), -2.152)
        p8 = Plane(Vector([2.016, -9.924, -1.367]), -9.278)
        p9 = Plane(Vector([2.167, -13.543, -18.883]), -10.567)

        l1 = LinearSystem([p6, p7, p8, p9])
        print('GE 3', l1.compute_gaussian_elimination())



if __name__ == '__main__':
    unittest.main()