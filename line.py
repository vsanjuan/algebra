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
            c = float(self.constant_term)
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            # print n
            # print "initial_index " + str(initial_index)
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

        return outputf64f7ba64503521c3d0e814157afd545cfa81454


    def is_paralel_to(self,line2):
        return self.normal_vector.is_paralel_to(line2.normal_vector)

    def __eq__(self,line2):
        base_point_line1 = self.basepoint
        base_point_line2 = line2.basepoint

        x = base_point_line1 - base_point_line2

        return x.is_orthogonal_to(self.normal_vector)

    def intersection(self,line2):


        A,B = self.normal_vector.coordinates
        C,D = line2.normal_vector.coordinates
        k1 = float(self.constant_term)
        k2 = float(line2.constant_term)

        if self.is_paralel_to(line2):
            #print A*D - B*C
            return False

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


x = Line(Vector([1.0,1]),1.0)
y = Line(Vector([2.0,2]),2)
z = Line(Vector([3.0,5]),1.0)


print x.normal_vector, type(x.normal_vector)
print x.basepoint, type(x.basepoint)

print x.is_paralel_to(y)
print x.is_paralel_to(z)

print x.__eq__(y)
print x.__eq__(z)

print x.intersection(y)
print x.intersection(z)

a,b = Line(Vector([4.046,2.836]),1.21),Line(Vector([10.115,7.09]),3.025)
c,d = Line(Vector([7.204,3.182]),8.68),Line(Vector([8.172,4.114]),9.883)
e,f = Line(Vector([1.182,5.562]),6.744), Line(Vector([1.773,8.343]),9.525)

print a.is_paralel_to(b), a.__eq__(b), a.intersection(b)
print "#" * 48
print c.is_paralel_to(d), c.__eq__(d), c.intersection(d)
print "#" * 48
print e.is_paralel_to(f), e.__eq__(f), e.intersection(f)
