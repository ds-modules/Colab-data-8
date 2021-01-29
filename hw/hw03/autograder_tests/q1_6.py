test = {   'name': 'q1_6',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> pter_over_time.take(0)\n'
                                               'Date       | NEI     | '
                                               'NEI-PTER | Year | PTER\n'
                                               '1994-01-01 | 10.0974 | '
                                               '11.172   | 1994 | 1.0746',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(pter_over_time.column("PTER") '
                                               '== pter)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(pter_over_time.column("Year") '
                                               '== year)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> pter_over_time.labels\n'
                                               "('Date', 'NEI', 'NEI-PTER', "
                                               "'Year', 'PTER')",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
