test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you have all '
                                               'the columns from both tables;\n'
                                               '>>> set(["Name", "Menu_Item", '
                                               '"Yelp", "Google", "Overall", '
                                               '"Cost"]) == '
                                               'set(burritos.labels)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> burritos.num_rows == 212\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "len(np.unique(burritos.group('Name').column(1)))\n"
                                               '10',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
