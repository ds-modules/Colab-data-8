test = {   'name': 'q2_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # Please don't edit the "
                                               'last line.;\n'
                                               '>>> latest_poverty.labels == '
                                               "('geo', 'time', "
                                               "'poverty_percent')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The result should have '
                                               'one row per country.;\n'
                                               '>>> latest_poverty.num_rows\n'
                                               '145',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(latest_poverty.sort('geo').take(np.arange(7, "
                                               '107, 10)))\n'
                                               'geo  | time | poverty_percent\n'
                                               'bdi  | 2006 | 81.32\n'
                                               'bra  | 2012 | 3.75\n'
                                               'cod  | 2006 | 87.72\n'
                                               'dom  | 2012 | 2.25\n'
                                               'fsm  | 2000 | 31.15\n'
                                               'guy  | 1998 | 8.7\n'
                                               'isr  | 2010 | 0.39\n'
                                               'lbr  | 2007 | 83.76\n'
                                               'mex  | 2012 | 1.03\n'
                                               'nga  | 2010 | 62.03\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
