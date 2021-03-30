test = {   'name': 'q4_2',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> summed_mn_data.num_rows \n'
                                               '2',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> len(summed_mn_data.labels) '
                                               '== 3\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'summed_mn_data.where("Condition", '
                                               '"Control").column("Died '
                                               'sum").item(0) == 222\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'summed_mn_data.where("Condition", '
                                               '"Diet").column("Died '
                                               'sum").item(0) == 245\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'summed_mn_data.where("Condition", '
                                               '"Control").column("Participated '
                                               'sum").item(0) == 4738\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'summed_mn_data.where("Condition", '
                                               '"Diet").column("Participated '
                                               'sum").item(0) == 4685\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
