test = {   'name': 'q1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> first = '
                                               'round(b_five_growth.sort(0).column(2).item(0), '
                                               '8);\n'
                                               '>>> 0.005 <= first <= 0.5\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Compute the annual '
                                               'exponential growth rate;\n'
                                               '>>> '
                                               'max(b_five_growth.column(2)) < '
                                               '0.03\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Compute the annual '
                                               'exponential growth rate;\n'
                                               '>>> '
                                               'np.allclose(np.round(sum(b_five_growth.column(2)), '
                                               '5), 0.18323)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Table does not have '
                                               'expected values;\n'
                                               '>>> '
                                               'round(b_five_growth.column(2).item(0), '
                                               '8) == 0.01837042\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(b_five_growth.column(2).item(3), '
                                               '8) == 0.02644713\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'round(b_five_growth.column(2).item(8), '
                                               '8) == 0.01207657\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
