test = {   'name': 'q1_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like your '
                                               "simulation isn't random.;\n"
                                               '>>> np.std([simulate() for _ '
                                               'in range(1000)]) > 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(possible_area_codes == '
                                               'np.arange(200, 1000))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.random.seed(10);\n'
                                               '>>> abs(np.mean([simulate() '
                                               'for _ in range(1000)]) - '
                                               '(1/16)) <= 0.02\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
