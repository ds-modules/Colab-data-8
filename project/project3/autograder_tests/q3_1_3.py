test = {   'name': 'q3_1_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> genre_and_distances.labels '
                                               "== ('Genre', 'Distance')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'genre_and_distances.num_rows '
                                               '== train_movies.num_rows\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(genre_and_distances.group('Genre'))\n"
                                               'Genre   | count\n'
                                               'action  | 114\n'
                                               'romance | 91\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.allclose(genre_and_distances.column('Distance'), "
                                               'sorted(fast_distances(test_20.row(0), '
                                               'train_20)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
