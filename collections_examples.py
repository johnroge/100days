#!/usr/bin/env python3
"""
Practice file for collections
"""
from collections import Counter, namedtuple, defaultdict, deque
import random
import csv
from urllib.request import urlretrieve

# named tuples example
User = namedtuple('User', 'name role')
user1 = User(name='bob', role='coder')
print(f'{user1.name} is a {user1.role}')

# defaultdict example
users = {'bob': 'coder'}
print(users.get('bob'))
print(users.get('sarah')) # this returns None rather than KeyError

# create a dict from the following tuples
challenges_done = [('mike', 10),
                   ('tom', 7),
                   ('bob', 12),
                   ('sarah', 2),
                   ('alex', 23),
                   ('sam', 3),
                   ('tess', 12),
                   ]

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

# find common words
# old way:
words = """The population of the city has increased tenfold since the
        1950s, as migrants from across Anatolia have moved in and
        city""".split()

common_words = {}
for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

for k, v in sorted(common_words.items(), key=lambda x: x[1],
                   reverse=True):
    print(k, v)

# new way
print(Counter(words).most_common(4))

# deque - insert and append on both sides of the sequence
lst = list(range(100000))
deq = deque(range(100000))


# deq is much faster than lst when run through the below function
def insert_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

# TODO: OrderedDict([items])
# TODO: ChainMap