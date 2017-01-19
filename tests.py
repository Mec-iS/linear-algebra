from math import degrees
from vector import Vector

v = Vector([1,2,3,7,9])
w = Vector([5,6,2,4,9,1,4,8,4])

v_ = v.multiply(3)

n = Vector([0,0,0,0,0,0])

def print_vectors():
    print('***Initial vectors***')
    print('class: ', v.__class__)
    print('|v|: ', v)
    print('|w|: ', w)
    print('|v_|: ', v_)
    print('---------------')

def print_null():
    print('***Null vector***')
    print('|n|: ', n)
    print('||n||: ', n.magnitude)
    print('---------------')

def print_operations():
    print('***Operations***')
    print('|v| + |w|: ', v.add(w))
    print('|v| - |w|: ', v.subtract(w))
    print('|w| = |v|: ', w.subtract(v))
    print('|v| * 3: ', v.multiply(3))
    print('|v| == |w|? ', v == w)
    print('---------------')

def print_magnitude_and_direction():
    print('***Magnitude and direction***')
    print('||v||: ', v.magnitude)
    print('||w||: ', w.magnitude)
    print('|u|v (unit of |v|): ', v.unit)
    print('|u|w (unit of |w|): ',w.unit)
    print('---------------')

def print_features():
    print('***Classes of vectors***')
    print('|v| is the same class of |w| (same unit/direction)? ', v.__same_class__(w))
    print('|v| is the same class of |v_| (same unit/direction)? ',v.__same_class__(v_))
    print('---------------')


#print_vectors()
#print_null()
#print_operations()
#print_magnitude_and_direction()
#print_features()

print('------- EXCERCISES --------')
a = Vector([8.218, -9.341])
b = Vector([-1.129, 2.111])

print('1', a.add(b))

c = Vector([7.119, 8.215])
d = Vector([-8.223, 0.878])

print('2', c.subtract(d))

e = Vector([1.671, -1.012, -0.318])
print('3', e.multiply(7.41))

if not a.add(b) == Vector([7.089, -7.229999999999999]):
    raise ValueError('Error in addition')

if not c.subtract(d) == Vector([15.342, 7.337]):
    raise ValueError('Error in subtraction')

if not e.multiply(7.41) == Vector([12.38211, -7.49892, -2.35638]):
    raise ValueError('Error in scalar multiplication')

a = Vector([-0.221, 7.437])
print(a.magnitude)

b = Vector([8.813, -1.331, -6.247])
print(b.magnitude)

a = Vector([5.581, -2.136])
print(a.unit)

a = Vector([1.996, 3.108, -4.554])
print(a.unit)

print('dot products')
a = Vector([7.887, 4.138])
b = Vector([-8.802, 6.776])
print(a.dot(b))

a = Vector([-5.955, -4.904, -1.874])
b = Vector([-4.496, -8.755, 7.103])
print(a.dot(b))

print('angles')
a = Vector([3.183, -7.627])
b = Vector([-2.668, 5.319])
print(a.angle(b))

a = Vector([7.35, 0.221, 5.188])
b = Vector([2.751, 8.259, 3.985])
print(degrees(a.angle(b)))





