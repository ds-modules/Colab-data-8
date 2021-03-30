test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Check your column labels '
                                               'and spelling;\n'
                                               ">>> b_pop.labels == ('time', "
                                               "'population_total')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Times should range from '
                                               '1970 through 2015;\n'
                                               '>>> '
                                               'all(b_pop.sort("time").column("time") '
                                               '== np.arange(1970, 2016))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> b_pop.sort("time", '
                                               'descending=True).column("population_total").item(0)\n'
                                               '160995642',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'b_pop.sort("time").column("population_total").item(0)\n'
                                               '65048701',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
