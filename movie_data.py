#!/usr/bin/env python3
"""
use defaultdict for movie database
"""
import csv
from collections import defaultdict, namedtuple, Counter

vie_data = 'https://raw.githubusercontent/com/pybites/challenges/' \
           'solutions/13/movie_metadata.csv'
vie_csv = 'moves.csv'


Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movies_csv):
    """
    Extract all movies from csv and store in dict
    :param data: movies_csv
    :return: defaultdict
    """
    directors = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors


# get a count of the top five
cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

cnt.most_common(5)

