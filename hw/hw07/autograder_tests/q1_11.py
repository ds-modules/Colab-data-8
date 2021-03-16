test = {   'name': 'q1_11',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like your '
                                               "simulation isn't random.;\n"
                                               '>>> '
                                               'np.std([simulate_visited_area_codes() '
                                               'for _ in range(1000)]) > 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The sum of the items in '
                                               'model proportions should be '
                                               '1;\n'
                                               '>>> model_proportions.item(0) '
                                               '+ model_proportions.item(1)\n'
                                               '1.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(10);\n'
                                               '>>> '
                                               'abs(np.mean([simulate_visited_area_codes() '
                                               'for _ in range(1000)]) - '
                                               '(1/2)) <= 0.2\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
