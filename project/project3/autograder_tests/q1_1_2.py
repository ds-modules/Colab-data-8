test = {   'name': 'q1_1_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "unstemmed_run.item(0).startswith('run')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(unstemmed_run) > 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.all(np.sort(unstemmed_run) '
                                               "== np.sort(make_array(['runs', "
                                               "'running', 'run', 'runned', "
                                               "'runnings'])))\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
