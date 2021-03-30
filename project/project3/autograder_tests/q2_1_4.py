test = {   'name': 'q2_1_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> set(close_movies.labels) '
                                               ">= {'Genre', 'Title', 'feel', "
                                               "'money'}\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> close_movies.num_rows == '
                                               '7\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> [title[:8] for title in '
                                               "close_movies.column('Title')] "
                                               "== ['the brid', 'the fish', "
                                               "'broadcas', 'hellboy', 'as "
                                               "good ', 'spider-m', 'harold "
                                               "a']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
