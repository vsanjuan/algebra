from vector import Vector

import math

from decimal import Decimal, getcontext

getcontext().prec = 30



####################################################################


#Par projection two is_paralel_to vectors
x = Vector([0,1])
y = Vector([0,-1])

print x.par_proj(y)
print x.ort_proj(y)

print x.angle(y)
print x.angle(y) / math.pi
print x.is_paralel_to(y)


# Vector product
a,b = Vector([8.462,7.893,-8.187]),Vector([6.984,-5.975,4.778])
c,d = Vector([-8.987,-9.838,5.031]),Vector([-4.268,-1.861,-8.866])
e,f = Vector([1.5,9.547,3.691]),Vector([-6.007,0.124,5.772])

print a.cross_product(b)
print c.cross_product(d).magnitude()
print e.cross_product(f).magnitude() /2


# coding vector projecttions

a,b = Vector([3.039,1.879]),Vector([0.825,2.036])
c,d = Vector([-9.88,-3.264,-8.159]),Vector([-2.155,-9.353,-9.473])
e,f = Vector([3.009,-6.172,3.692,-2.51]),Vector([6.404,-9.144,2.759,8.718])

print a.par_proj(b)
print a == a.par_proj(b) + a.ort_proj(b)
print c.ort_proj(d)
print e.par_proj(f)
print e.ort_proj(f)


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

# dot product
k,j = Vector([7.887,4.138]),Vector([-8.802,6.776])
l,m = Vector([-5.955,-4.904,-1.874]),Vector([-4.496,-8.755,7.103])

print k.dot(j)
print l.dot(m)

#angle between vectors
n,o = Vector([1,1]),Vector([2,2])
q = Vector([-1,-1])

print n.dimension, o.dimension
print type(o) == Vector

print math.degrees(n.angle(o))
print math.degrees(n.angle(q))

r, s = Vector([3.183,-7.627]),Vector([-2.668,5.319])
t, u = Vector([7.35,0.221,5.188]),Vector([2.751,8.259,3.985])

print r.angle(s)
print math.degrees(t.angle(u))

#is_paralel_to or orthogonal

a, b = Vector([-7.579,-7.88]),Vector([22.737,23.64])
c, d = Vector([-2.029,9.97,4.172]),Vector([-9.231,-6.639,-7.245])
e, f = Vector([-2.328,-7.284,-1.214]),Vector([-1.821,1.072,-2.94])
g, h = Vector([2.118,4.827]),Vector([0,0])

print math.degrees(a.angle(b))
print math.degrees(c.angle(d))
print math.degrees(e.angle(f))
print g.angle(h)

