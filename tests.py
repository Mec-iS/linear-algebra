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


print_vectors()
print_null()
print_operations()
print_magnitude_and_direction()
print_features()


