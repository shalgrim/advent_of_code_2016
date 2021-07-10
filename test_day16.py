from day16_1 import checksum, generate, main


def test_generate():
    assert generate('1') == '100'
    assert generate('0') == '001'
    assert generate('11111') == '11111000000'
    assert generate('111100001010') == '1111000010100101011110000'


def test_checksum():
    assert checksum('110010110100') == '100'


def test_main():
    assert main('10000', 20) == '01100'
