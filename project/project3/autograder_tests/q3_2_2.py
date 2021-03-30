test = {   'name': 'q3_2_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> from collections import '
                                               'Counter;\n'
                                               '>>> g = '
                                               "train_movies.column('Genre');\n"
                                               '>>> r = '
                                               "np.where(test_movies['Title'] "
                                               '== "king kong")[0][0];\n'
                                               '>>> t = test_20.row(r);\n'
                                               '>>> king_kong_expected_genre = '
                                               'Counter(np.take(g, '
                                               'np.argsort(fast_distances(t, '
                                               'train_20))[:11])).most_common(1)[0][0];\n'
                                               '>>> king_kong_genre == '
                                               'king_kong_expected_genre\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
