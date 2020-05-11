from day03_1 import is_possible_triangle


def verticalize(ints):
    verticals = []
    for i in range(0, len(ints), 3):
        for j in range(3):
            verticals.append([ints[i][j], ints[i+1][j], ints[i+2][j]])

    return verticals


if __name__ == '__main__':
    with open('data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    ints = [[int(x) for x in row.split()] for row in lines]
    vertical_triangles = verticalize(ints)
    possibles = [is_possible_triangle(vert) for vert in vertical_triangles]
    print(sum(possibles))  # 1836 is too low...wild because the input is only 1908 lines long...nope, 1836 is right wth
