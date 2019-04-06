#!/usr/bin/env python3
"""
find duplicates using a dictionary of hashes
version .1
last updated: 4/2019
"""
import glob
import hashlib


def main():
    """
    main program loop
    :return: list of duplicate files
    """


# get some user input and instantiate the lists and dict
print('Please enter a path to search: ')
folders_to_search = input('Example: \\test\*.jpg \n')
my_files = {}
list_of_duplicates = []
photos = []

# build a list of files
for file in glob.glob(folders_to_search):
    photos.append(file)

# create a dict using the file name and hash
# TODO: each hash is unique, including duplicates - why?
hasher = hashlib.md5()
for f in photos:
    with open(f, 'rb') as a_file:
        buf = a_file.read()
        hasher.update(buf)
        if hasher.hexdigest() in my_files:
            list_of_duplicates.append(f)
            list_of_duplicates.append(my_files[hasher.hexdigest()])
        else:
            my_files.update({hasher.hexdigest(): f})


print(my_files)
print()
print(list_of_duplicates)


if __name__ == '__main__':
    main()
