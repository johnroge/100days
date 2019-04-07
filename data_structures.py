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

# dict
my_files = {}
some_list = []
list_of_files = sys_command??

for f in list_of_files:
    file_hash = md5hashFunction(f) # need to find this function
    file_path = sys_command??(f)
    if file_hash in my_files:
        some_list.append(f.file_path)
        some_list.append(my_files[file_hash][]) # need syntax here
    else:
        my_files[file_hash] = f.file_path