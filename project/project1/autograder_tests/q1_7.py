test = {   'name': 'q1_7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you are using '
                                               'the date range 1970-2015;\n'
                                               '>>> '
                                               'post_1969_fertility_and_child_mortality.num_rows\n'
                                               '46',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check your column labels '
                                               'and spelling;\n'
                                               '>>> all([label in '
                                               'post_1969_fertility_and_child_mortality.labels '
                                               "for label in ['Children per "
                                               "woman', 'Child deaths per 1000 "
                                               "born']])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(1).item(0), '
                                               '224.1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(1).item(-1), '
                                               '37.6)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(0).item(-1), '
                                               '2.12)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(0).item(0), '
                                               '6.95)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(1).mean(), '
                                               '131.41521739130437)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> facm = '
                                               "post_1969_fertility_and_child_mortality.select('Children "
                                               "per woman', 'Child deaths per "
                                               "1000 born');\n"
                                               '>>> '
                                               'np.allclose(facm.column(0).mean(), '
                                               '4.3958695652173922)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
