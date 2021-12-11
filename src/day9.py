import numpy as np


def find_lows(lavatubes):
    left = np.less(lavatubes[1:-1, 1:-1], lavatubes[1:-1, 0:-2])
    right = np.less(lavatubes[1:-1, 1:-1], lavatubes[1:-1, 2:])
    up = np.less(lavatubes[1:-1, 1:-1], lavatubes[0:-2, 1:-1])
    down = np.less(lavatubes[1:-1, 1:-1], lavatubes[2:, 1:-1])
    mask = left & right & up & down
    print(sum(lavatubes[1:-1, 1:-1][mask]) + len(lavatubes[1:-1, 1:-1][mask]))


if __name__ == "__main__":
    with open("data/day9test.txt") as fp:
        horizontal = list(np.full((12), 10))
        lavalist = [horizontal]
        for line in fp:
            row = list(line.rstrip())
            row.insert(0, 10)
            row.append(10)
            lavalist.append(row)
        lavalist.append(horizontal)
        lavatubes = np.array(lavalist, dtype=np.int64)
        print(lavatubes)
        find_lows(lavatubes)
