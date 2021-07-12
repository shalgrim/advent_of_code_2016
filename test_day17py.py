from day17_1 import find_shortest_path


def test_find_shortest_path():
    assert find_shortest_path('ihgpwlah') == 'DDRRRD'
    assert find_shortest_path('kglvqrro') == 'DDUDRLRRUDRD'
    assert find_shortest_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
