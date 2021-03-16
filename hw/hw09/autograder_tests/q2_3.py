test = {   'name': 'q2_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(example_estimates) == '
                                               '10000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> 850 < '
                                               'np.mean(example_estimates) < '
                                               '1100\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.count_nonzero(np.diff(example_estimates)) '
                                               '>= 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(123);\n'
                                               '>>> '
                                               'np.mean(sample_estimates(one_sample, '
                                               'mean_based_estimator, 10000))\n'
                                               '897.954712',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
