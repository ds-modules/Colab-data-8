test = {   'name': 'q2_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Check your column labels '
                                               'and spelling;\n'
                                               ">>> largest.labels == ('name', "
                                               "'poverty_total')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # India is the country '
                                               'with the largest number of '
                                               'people living;\n'
                                               '>>> # in extreme poverty.;\n'
                                               '>>> largest.column(0).item(0)\n'
                                               "'India'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The table should contain '
                                               'exactly 10 rows.;\n'
                                               '>>> largest.num_rows\n'
                                               '10',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'print(largest.take(np.arange(3)).column(1))\n'
                                               '[2.90881638e+08 9.88911670e+07 '
                                               '8.39446430e+07]\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
