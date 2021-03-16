test = {   'name': 'q1_20',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'all([type(lower_bound_evan) in '
                                               'set([float, np.float32, '
                                               'np.float64]), \n'
                                               '...     type(upper_bound_evan) '
                                               'in set([float, np.float32, '
                                               'np.float64])])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([lower_bound_evan == '
                                               'percentile(0.5, '
                                               'resampled_predictions), \n'
                                               '...      upper_bound_evan == '
                                               'percentile(99.5, '
                                               'resampled_predictions)])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
