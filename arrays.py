from array import *
a1 = array('i', [1, 47, 33, 74, 38939, 339, 3839, 74])
a2 = array('i', [23, 34, 55, 45])
print(a1[4])
print(a1.index(74))  # returns index of a value
print(a1.index(74, 1, 7))
from lists import l1
print(a1)
print(a1.insert(1, 3435))
print(a1)
print(a1.count(74))
print(a1.fromlist(l1))  # appending values to an array from a list
print(a1)
print(a1.append(66))
print(a1)
a1.extend(a2)  # add an array to the other
print(a1)
a1.reverse()
print(a1)
print(len(a1))
a1.remove(1)
print(a1)
l7 = a1.tolist()  # converts an array to a list
print(l7)
print(a1.buffer_info())
