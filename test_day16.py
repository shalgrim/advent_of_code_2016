from day16_1 import generate


def test_generate():
    assert generate('1') == '100'
    assert generate('0') == '001'
    assert generate('11111') == '11111000000'
    assert generate('111100001010') == '1111000010100101011110000'
