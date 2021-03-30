test = {   'name': 'q2_2_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'isinstance(compute_framingham_test_statistic(framingham), '
                                               '(float, int, np.integer))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> fake_framingham1 = '
                                               "Table().with_columns('TOTCHOL', "
                                               'make_array(200, 225, 250, '
                                               "275), 'ANYCHD', make_array(1, "
                                               '0, 0, 1));\n'
                                               '>>> fake_framingham2 = '
                                               "Table().with_columns('TOTCHOL', "
                                               'make_array(200, 225, 250, '
                                               "275), 'ANYCHD', make_array(0, "
                                               '0, 1, 1));\n'
                                               '>>> '
                                               'compute_framingham_test_statistic(fake_framingham1) '
                                               '< '
                                               'compute_framingham_test_statistic(fake_framingham2)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.isclose(round(framingham_observed_statistic, '
                                               '3), 16.636)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
