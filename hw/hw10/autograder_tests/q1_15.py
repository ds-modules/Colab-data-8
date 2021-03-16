test = {   'name': 'q1_15',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> len(minimized_parameters) '
                                               '== 2\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure to input '
                                               '`smooth=True` as the second '
                                               'argument to the `minimize` '
                                               'function;\n'
                                               '>>> # i.e. minimize(..., '
                                               'smooth=True);\n'
                                               '>>> (1 <= '
                                               'minimized_parameters.item(0) '
                                               '<= 2) and (-7 <= '
                                               'minimized_parameters.item(1) '
                                               '<= -6)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.allclose(minimized_parameters, '
                                               '[1.07113932, -6.4542811])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
