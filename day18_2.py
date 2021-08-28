from day18_1 import build_map, num_safe_tiles

if __name__ == '__main__':
    with open('data/input18.txt') as f:
        row = f.read().strip()
    map = build_map(row, 400_000)
    print(num_safe_tiles(map))
