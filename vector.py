class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, j):
        try:
            if not self.dimension == j.dimension:
                raise ValueError
            addition = []
            for i in range(self.dimension):
                    addition.append(self.coordinates[i] + j.coordinates[i])

            return Vector(addition)

        except ValueError:
            raise ValueError('Two add two vectors must have same dimensions')

    def __sub__(self, j):
        try:
            if not self.dimension == j.dimension:
                raise ValueError
            substraction = []
            for i in range(self.dimension):
                substraction.append(self.coordinates[i] - j.coordinates[i])

            return Vector(substraction)

        except ValueError:
            raise ValueError('Two substract two vectors must have same dimensions')

    def __mul__(self, j):
        try:
            if not type(j*1.0) == float:
                raise ValueError
            value = []
            for coor_v in self.coordinates:
                    value.append(coor_v * j)

            return Vector(value)

        except ValueError:
            raise ValueError('A vector must be multiplied by a number')

    def magnitude(self):
        magn = 0
        for coor in self.coordinates:
            magn += coor ** 2

        return magn ** (0.5)

    def normal(self):
        magn = self.magnitude()
        normal_vector = []

        for coor in self.coordinates:
            normal_vector.append(coor/magn)

        return Vector(normal_vector)






a = Vector([8.218,-9.341])
b = Vector([-1.129,2.111])

c = Vector([7.119,8.215])
d = Vector([-8.223,0.878])

e = Vector([1.671,-1.012,-0.318])

f = Vector([-0.221,7.437])
g = Vector([5.581,-2.136])

h = Vector([8.813,-1.331,-6.247])
j = Vector([1.996,3.108,-4.554])


print a + b
print c - d
print e * 7.41
print f.magnitude()
print h.magnitude()
print g.normal()
print j.normal()

print g.normal().magnitude()
print j.normal().magnitude()
