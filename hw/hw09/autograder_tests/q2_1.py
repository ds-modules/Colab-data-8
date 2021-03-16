test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Your resample should '
                                               'have the same number of rows '
                                               'as the original sample;\n'
                                               '>>> '
                                               'simulate_resample(observations).num_rows\n'
                                               '17',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Your resample should '
                                               'only have the ;\n'
                                               '>>> '
                                               'simulate_resample(observations).labels[0] '
                                               '== observations.labels[0] \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # This is a little magic '
                                               'to make sure that you see the '
                                               'same results;\n'
                                               '>>> # we did.;\n'
                                               '>>> np.random.seed(123);\n'
                                               '>>> \n'
                                               '>>> one_resample = '
                                               'simulate_resample(observations);\n'
                                               '>>> ten_rows = '
                                               'one_resample.take(np.arange(10));\n'
                                               '>>> ten_rows\n'
                                               'serial number\n'
                                               '108\n'
                                               '57\n'
                                               '57\n'
                                               '36\n'
                                               '41\n'
                                               '42\n'
                                               '47\n'
                                               '50\n'
                                               '135\n'
                                               '47',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
