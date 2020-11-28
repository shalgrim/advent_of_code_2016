from hashlib import md5
from day14_1 import my_md5, get_triple_char


def stretched_md5(num):
    answer = my_md5(num)
    for _ in range(2016):
        m = md5()
        ba = bytearray(answer, 'utf-8')
        m.update(ba)
        answer = m.hexdigest()

    return answer


def generate_hashes():
    i = 0
    while True:
        yield i, stretched_md5(i)
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
