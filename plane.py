from decimal import Decimal, getcontext
import math

from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = float(self.constant_term)
            # c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            # initial_coefficient = n[initial_index]
            initial_coefficient = float(n[initial_index])

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def __mul__(self, j):


        # print self.normal_vector, self.constant_term, j

        normal_vector = self.normal_vector * j
        constant_term = self.constant_term * j

        # print normal_vector

        return Plane(normal_vector,constant_term)

    def is_paralel_to(self, plane2):
        # print math.degrees(self.normal_vector.angle(plane2.normal_vector))
        return self.normal_vector.is_paralel_to(plane2.normal_vector)

    def __eq__(self,plane2):

        if not self.is_paralel_to(plane2):
            return False

        plane_basepoint = self.basepoint
        plane2_basepoint = plane2.basepoint

        # print plane_basepoint, plane2_basepoint

        vector_basepoint = plane_basepoint - plane2_basepoint

        if vector_basepoint.is_zero():
            return True

        return self.normal_vector.is_orthogonal_to(vector_basepoint)

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


# Check equality operator after multiplying

# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')


# print p2.normal_vector, p2.constant_term
# print p2.normal_vector == Vector([-1,-1,1])
# print p2 == Plane(Vector(['-1','-1','1']),-3) 
# print p0 == p2
# print p0 == p1 


# Check equality and paralelism

# a = Plane(Vector(['1.0','1.0','1.0']),'1')
# b = Plane(Vector([2,2,2]),2)
# c = Plane(Vector([2,2,2]),5)
# d = Plane(Vector([3,4,7]),3)

# print a.normal_vector, a.constant_term, a.basepoint

# print a * 3 


# print a.is_paralel_to(b)
# print a.is_paralel_to(c)
# print d.is_paralel_to(a)

# print a == b
# print a == c
# print a == d

# print "*" * 64

# a,b = Plane(Vector([-0.412,3.806,0.728]),-3.46),Plane(Vector([1.03,-9.515,-1.82]),8.65)
# c,d = Plane(Vector([2.611,5.528,0.283]),4.6),Plane(Vector([7.715,8.306,5.342]),3.76)
# d,e = Plane(Vector([-7.926,8.625,-7.212]),-7.952),Plane(Vector([-2.642,2.875,-2.404]),-2.443)

# print "*" * 64
# # print a.normal_vector.angle(b.normal_vector)
# print a.is_paralel_to(b), a == b
# print "*" * 64
# print c.is_paralel_to(d), c == d
# print "*" * 64
# print d.is_paralel_to(e), d == e

# p = Vector([1,1,1])

# print Plane.first_nonzero_index(p)