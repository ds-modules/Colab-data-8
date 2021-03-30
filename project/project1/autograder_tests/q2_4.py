test = {   'name': 'q2_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # Check your column labels '
                                               'and spelling;\n'
                                               '>>> poverty_map.labels == '
                                               "('latitude', 'longitude', "
                                               "'name', 'region', "
                                               "'poverty_total')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Something is wrong with '
                                               'your region column.;\n'
                                               '>>> '
                                               "list(np.sort(np.unique(poverty_map.column('region'))))\n"
                                               "['africa', 'americas', 'asia', "
                                               "'europe']",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "print(poverty_map.sort('name').take(np.arange(10)).drop(4))\n"
                                               'latitude | longitude | '
                                               'name       | region\n'
                                               '41       | 20        | '
                                               'Albania    | europe\n'
                                               '28       | 3         | '
                                               'Algeria    | africa\n'
                                               '-12.5    | 18.5      | '
                                               'Angola     | africa\n'
                                               '-34      | -64       | '
                                               'Argentina  | americas\n'
                                               '40.25    | 45        | '
                                               'Armenia    | europe\n'
                                               '-25      | 135       | '
                                               'Australia  | asia\n'
                                               '47.3333  | 13.3333   | '
                                               'Austria    | europe\n'
                                               '40.5     | 47.5      | '
                                               'Azerbaijan | europe\n'
                                               '24       | 90        | '
                                               'Bangladesh | asia\n'
                                               '53       | 28        | '
                                               'Belarus    | europe\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sum(poverty_map.column(4)) '
                                               '== '
                                               'sum(recent_poverty_total.column(3))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
