from day17_1 import find_shortest_path
from day17_2 import find_longest_path_length


def test_find_shortest_path():
    assert find_shortest_path('ihgpwlah') == 'DDRRRD'
    assert find_shortest_path('kglvqrro') == 'DDUDRLRRUDRD'
    assert find_shortest_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def test_find_longest_path_length():
    assert find_longest_path_length('ihgpwlah') == 370
    assert find_longest_path_length('kglvqrro') == 492
    assert find_longest_path_length('ulqzkmiv') == 830
