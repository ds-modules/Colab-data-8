test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> prof_names.num_columns\n2',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> prof_names.num_rows\n71',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that you have '
                                               'the correct column labels!;\n'
                                               '>>> '
                                               'np.asarray(prof_names.labels).item(1) '
                                               '!= "name identity"\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Make sure that you have '
                                               'the correct column labels!;\n'
                                               '>>> '
                                               'np.asarray(prof_names.labels).item(1) '
                                               '== "faculty"\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "len(prof_names.where('department', "
                                               "'Computer "
                                               "Science').column('faculty').item(0))\n"
                                               '46',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "len(prof_names.where('department', "
                                               "'Mathematics').column('faculty').item(0))\n"
                                               '48',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
