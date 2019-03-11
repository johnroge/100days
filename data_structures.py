#!/usr/bin/env python3
"""
examples of data structures, 100 days of python
"""

# manipulating lists
numlist = [1, 2, 3, 4, 5]
numlist.reverse()
numlist.sort()
print(numlist)

mystring = 'julian'
l = list(mystring)
print(l)
print(l[0])
l.pop()
print(l)

l.insert(5, 'n')
l[0] = 'b'
l.pop(0)
print(l)

