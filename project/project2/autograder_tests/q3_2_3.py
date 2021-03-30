test = {   'name': 'q3_2_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(HERS_test_statistics) '
                                               '== 1000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 0<= '
                                               'min(HERS_test_statistics) <= '
                                               '0.055\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(49);\n'
                                               '>>> '
                                               'np.isclose(round(simulate_one_HERS_statistic(), '
                                               '5), 0.00697) \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
