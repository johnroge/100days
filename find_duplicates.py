#!/usr/bin/env python3
"""
deletes duplicates using a dictionary of hashes
version 1.0
last updated: 4/2019
author: Andres Torres
"""
import os
import sys
import hashlib


def main():
    """
    main script logic
    :return: currently deletes all subsequent duplicate files found
    """
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            if os.path.exists(i):
                join_dict(dups, find_dup(i))
            else:
                print('%s is not a valid path' % i)
                sys.exit()
        print_results(dups)
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


def find_dup(folder_to_search):
    """
    scan folder and sub-folders for duplicate files
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
                dups[file_hash].append(path)
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


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates found: ')
        print('following files are identical:')
        print('-' * 60)
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('-' * 60)
    else:
        print('No duplicates found.')


if __name__ == '__main__':
    main()
