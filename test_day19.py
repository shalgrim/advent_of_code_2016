from day19_1 import main
from day19_2 import main as main2


def test_part_1():
    assert main(5) == 3
    assert main(3_005_290) == 1_816_277


def test_part_2():
    assert main2(5) == 2
