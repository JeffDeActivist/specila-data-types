l1 = [1, 2, 2, 2, 2, 3, 4, 56, 56, 46, 58, 47, 473, 83, 377, 3737]
l2 = [53, 37, 37, 37, 38]
print(l1[::-1])  # to reverse a list
l1.append(2)
print(l1)
print(l1[1::2])  # skipping values in a list
l1.extend(l2)
print(l1)
# pop removes an element in the specified index, last index by default
print(l1.pop())
print(l1)
print(l1.pop(2))
print(l1)
print(l1.clear())  # clears contents of the list
print(l1)
print(l1.reverse())
print(l1)  # returns a reverse of a list
print(l1.remove(1))  # removes fist value in the list that is specified
print(l1)
print(l1.index(56, 1, 5))   # returns the index of the first item
print(l1)
print(l1.count(56))  # returns the number of counts for a value specified
for i in l1:
    if i == 377:
        break
    print(i)
l3 = l1.copy()  # copying a list to another one
print(l3)
print(sorted(l1))  #sorts in an ascending order
# this is an append from the file handling tutorial
from collections import Counter
ll1 = Counter(l1)  # returns the count of each item in a list
print(ll1)
import heapq
print(heapq.nlargest(2, l1))  # returns 2 highest values in the list
l1.sort(reverse=False)
print(l1)
