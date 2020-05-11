# def is_possible_triangle(measurements):
#     max_val = max(measurements)
#     measurements.remove(max_val)
#     return sum(measurements) > max_val


def is_possible_triangle(measurements):
    if (
        measurements[0] + measurements[1] > measurements[2]
        and measurements[0] + measurements[2] > measurements[1]
        and measurements[1] + measurements[2] > measurements[0]
    ):
        return True
    return False


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    ints = [[int(x) for x in row.split()] for row in lines]
    possibles = [is_possible_triangle(measurements) for measurements in ints]
    print(sum(possibles))
