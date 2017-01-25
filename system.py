from math import isclose

from plane import Plane

class LinearSystem(object):
    __ROUNDING = 9

    def __init__(self, planes):
        if not all(p.dimension == planes[0].dimension for p in planes): 
            raise ValueError('all planes must have the same dimension')
        self.planes = planes

    @property
    def dimension(self):
        return self.planes[0].dimension

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row, rounding=__ROUNDING):
        n = self[row].normal
        k = self[row].constant

        new_normal = n.multiply(coefficient)
        new_const = round(k * coefficient, rounding)

        self[row] = Plane(
            normal_vector=new_normal, 
            const_term=new_const
        )


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to, rounding=__ROUNDING):
        n1 = self[row_to_add].normal
        n2 = self[row_to_be_added_to].normal
        k1 = self[row_to_add].constant
        k2 = self[row_to_be_added_to].constant

        new_normal = n1.multiply(coefficient).add(n2)
        new_const = round((k1 * coefficient) + k2, rounding)

        self[row_to_be_added_to] = Plane(
            normal_vector=new_normal, 
            const_term=new_const
        )

    def swap_with_row_below(self, row, col, system):
        """
        Swap the equation with the one below if the coefficient is not zero.
        """
        num_equations = len(system)

        for k in range(row+1, num_equations):
            coefficient = self[k].normal[col]
            if not isclose(coefficient, 0):
                self.swap_rows(row, k)
                return True
        return False

    def clear_coefficients_below(self, row, col, system, rounding=__ROUNDING):
        """
        Calculate the alpha value to clear each row k underneath the given row
        """
        num_equations = len(system)
        beta = self[row].normal[col]

        for k in range(row+1, num_equations):
            n = self[k].normal
            gamma = n[col]
            alpha = round(-gamma / beta, rounding)
            self.add_multiple_times_row_to_row(alpha, row, k)
            

    def compute_triangular_form(self):
        from copy import deepcopy

        system = deepcopy(self)

        num_equations = len(system)
        num_variables = system.dimension

        j = 0
        for i in range(num_equations):
            while j < num_variables:
                c = system[i].normal[j]
                if isclose(c, 0):
                    if not system.swap_with_row_below(i, j, system):
                        j += 1
                        continue
                system.clear_coefficients_below(i, j, system)
                break

        return system

    def scale_row_to_cofficient_equal_one(self, row, col, rounding=__ROUNDING):
        n = self[row].normal
        print(self[row].normal)
        print(n[col])
        beta = round(1 / n[col], rounding)
        self.multiply_coefficient_and_row(beta, row)

    def clear_coefficients_above(self, row, col):
        for k in range(row)[::-1]:
            n = self[k].normal
            alpha = - (n[col])
            self.add_multiple_times_row_to_row(alpha, row, k)

    def compute_rref(self):
        """
        Compute the system into a reduced row-ecehlon form
        """
        tf = self.compute_triangular_form()

        num_equations = len(tf)
        pivots = tf.indices_of_first_nonzero_terms_in_each_row()

        for i in range(num_equations)[::-1]:
            j = pivots[i]
            if j < 0:
                continue
            tf.scale_row_to_cofficient_equal_one(i, j)
            tf.clear_coefficients_above(i, j)

        return tf

    def compute_gaussian_elimination(self):
        try:
            return self.do_gaussian_elimination()
        except Exception as e:
            if (str(e) == 'No solutions' or 
                str(e) == 'Infinite solutions'):
                return str(e)
            else: raise e

    def do_gaussian_elimination(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory()
        rref.raise_exception_if_too_pivots()

        num_variables = rref.dimension
        solution_coordinates = [rref.planes[i].constant for i in range(num_variables)]

        return Vector(solution_coordinates)

    def raise_exception_if_contradictory(self):      
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal)
            except Exception as e:
                if not isclose(p.constant, 0):
                    raise Exception('No Solutions')
                else: raise e

    def raise_exception_if_too_pivots(self):
        pivots = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivots])
        num_variables = self.dimension

        if num_pivots < num_variables:
            raise Exception('Infinite solutions')


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except ValueError as e:
                continue
            except Exception as e:
                raise e

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        if not x.dimension == self.dimension:
            raise ValueError('plane has wrong dimension for the system')
        self.planes[i] = x

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret
