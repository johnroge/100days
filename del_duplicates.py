#!/usr/bin/env python3
"""
deletes duplicates using a dictionary of hashes
version 1.0
last updated: 4/2019
"""
import os
import sys
import hashlib
import time


def main():
    """
    main script logic; get user input for folder structure to scan
    :return: deletes all subsequent duplicate files found
    """

    # present the user with fair warning and chance to opt out
    print('This will delete all duplicate files found in the folder'
          ' structure!')
    print('-' * 60)
    print('-' * 60)
    time.sleep(6)
    print('Are you SURE you want to delete all the duplicates?')
    time.sleep(5)
    answer = input('If you still want to proceed, press Y. Any other'
                   ' key will exit the program:  ')

    if answer == 'Y':
        pass
    else:
        sys.exit()

    # walk a given folder path and
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            if os.path.exists(i):
                join_dict(dups, del_dup(i))
            else:
                print('%s is not a valid path' % i)
                sys.exit()
        print('all duplicate files have been deleted')
    else:
        print('usage: python find_duplicates.py folder1 folder2 folder3')


def hash_file(path, blocksize=65536):
    """
    get the md5 hash for a given file
    :param path: path to file to hash
    :param blocksize:
    :return: md5 hash of given file
    """
    a_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = a_file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = a_file.read(blocksize)
    a_file.close()
    return hasher.hexdigest()


def del_dup(folder_to_search):
    """
    scan folder and sub-folders and delete duplicate files
    :param folder_to_search: path to top level folder to search
    :return: a dictionary of file hashes and names
    """
    dups = {}

    for dir_name, subdirs, filelist in os.walk(folder_to_search):
        print(f'scanning {dir_name}...')
        for filename in filelist:
            path = os.path.join(dir_name, filename)
            file_hash = hash_file(path)
            if file_hash in dups:
                os.remove(path)
            else:
                dups[file_hash] = [path]

    return dups


def join_dict(dict1, dict2):
    """
    join two dictionaries
    :param dict1: first dictionary
    :param dict2: second dictionary
    :return: first dictionary as a superset of the two dicts
    """
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


if __name__ == '__main__':
    main()