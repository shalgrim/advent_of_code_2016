from hashlib import md5
import re

TRIPLE = re.compile(r'(.)\1\1')


SALT = 'cuanljph'  # actual
# SALT = 'abc'  # example
KNOWN_HASHES = {}


def my_md5(num):
    m = md5()
    s = SALT + str(num)
    ba = bytearray(s, 'utf-8')
    m.update(ba)
    return m.hexdigest()


def get_triple_char(s):
    match = TRIPLE.search(s)
    if match is None:
        return None
    return s[match.start()]


def generate_hashes():
    i = 0
    while True:
        yield i, my_md5(i)
        i += 1


def generate_keys():
    num_keys = 0
    hashes = {}
    triples = {}
    for index, hash in generate_hashes():
        hashes[index] = hash
        if char := get_triple_char(hash):
            triples[index] = char

        if fivechar := triples.get(index - 1000):
            fivestring = fivechar * 5
            for x in range(1000):
                if fivestring in hashes[index - x]:
                    num_keys += 1
                    yield index - 1000, hash
                    break

            if num_keys == 64:
                raise StopIteration


if __name__ == '__main__':
    for index, key in generate_keys():
        print(index, key)
