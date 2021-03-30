test = {   'name': 'q2_1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you can use '
                                               'any two movies;\n'
                                               '>>> correct_dis = '
                                               '0.0011432060212606049;\n'
                                               '>>> dis = '
                                               'distance_two_features("titanic", '
                                               '"the avengers", "money", '
                                               '"feel");\n'
                                               '>>> np.isclose(dis, '
                                               'correct_dis)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure you can use '
                                               'any two features;\n'
                                               '>>> correct_dis = '
                                               '0.0041988885973385463;\n'
                                               '>>> dis = '
                                               'distance_two_features("titanic", '
                                               '"the avengers", "your", '
                                               '"that");\n'
                                               '>>> np.isclose(dis, '
                                               'correct_dis)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
