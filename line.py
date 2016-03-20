from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

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
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            print n
            print "initial_index " + str(initial_index)
            initial_coefficient = n[initial_index]   # Takes one element from
            # the normal vector if is zero

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
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

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
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


    def paralel(self,line2):
        ang = self.normal_vector.angle(line2.normal_vector)
        return ang < 1e-5

    def same_line(self,line2):
        base_point_line1 = self.basepoint
        base_point_line2 = line2.basepoint

        x = base_point_line1 - base_point_line2

        y = Decimal(x.dot(self.normal_vector))
        print y

        return y == 0

    def intersection(self,line2):
        if self.paralel(line2):
            return False

        A = self.normal_vector.coordinates[0]
        B = self.normal_vector.coordinates[1]
        C = line2.normal_vector.coordinates[0]
        D = line2.normal_vector.coordinates[1]
        k1 = self.constant_term
        k2 = self.constant_term

        x = (D*k1-B*k2)/(A*D-B*C)
        y = (-C*k1+A*k2)/(A*D-B*C)

        return Vector([x,y])

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


# x = Line(Vector([1,1]),1)
# y = Line(Vector([2,2]),2)
# z = Line(Vector([3,5]),1)
#
#
# print x.normal_vector, type(x.normal_vector)
# print x.basepoint, type(x.basepoint)
#
# print x.paralel(y)
# print x.paralel(z)
#
# print x.same_line(y)
# print x.same_line(z)
#
# print x.intersection(y)
# print x.intersection(z)
