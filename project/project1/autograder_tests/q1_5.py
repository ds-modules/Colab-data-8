test = {   'name': 'q1_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Check your column labels '
                                               'and spelling;\n'
                                               ">>> fertility_over_time('usa', "
                                               "2010).labels == ('Year', "
                                               "'Children per woman')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the '
                                               'start year to determine the '
                                               'data range.;\n'
                                               '>>> '
                                               "all(fertility_over_time('usa', "
                                               "2010).column('Year') == "
                                               'np.arange(2010, 2016))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Check that you use the '
                                               'start year to determine the '
                                               'data range.;\n'
                                               '>>> '
                                               "all(fertility_over_time('usa', "
                                               "2005).column('Year') == "
                                               'np.arange(2005, 2016))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(fertility_over_time('bgd', "
                                               '2009))\n'
                                               'Year | Children per woman\n'
                                               '2009 | 2.32\n'
                                               '2010 | 2.28\n'
                                               '2011 | 2.24\n'
                                               '2012 | 2.21\n'
                                               '2013 | 2.18\n'
                                               '2014 | 2.15\n'
                                               '2015 | 2.12\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(fertility_over_time('usa', "
                                               '2010))\n'
                                               'Year | Children per woman\n'
                                               '2010 | 1.93\n'
                                               '2011 | 1.9\n'
                                               '2012 | 1.9\n'
                                               '2013 | 1.98\n'
                                               '2014 | 1.97\n'
                                               '2015 | 1.97\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
