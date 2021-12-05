import numpy as np


def setup(size):
    return np.zeros((size, size))


def read_input(filename, ocean, diagonals=True):
    with open(filename) as fp:
        for line in fp:
            start = np.array(line.rstrip().split()[0].split(",")).astype(np.int64)
            end = np.array(line.rstrip().split()[2].split(",")).astype(np.int64)
            if start[0] == end[0]:
                # x is the same, y varies
                direction = 1 if end[1] > start[1] else -1
                for i in range(start[1], end[1] + direction, direction):
                    ocean[i, start[0]] += 1
            elif start[1] == end[1]:
                # y is the same, x varies
                direction = 1 if end[0] > start[0] else -1
                for j in range(start[0], end[0] + direction, direction):
                    ocean[start[1], j] += 1
            elif diagonals:
                # diagonal line
                print(f"diagonal line: {start},{end}")
                left = start if end[1] > start[1] else end
                right = end if end[1] > start[1] else start
                direction = 1 if right[0] > left[0] else -1
                for i, j in zip(
                    range(left[1], right[1] + 1),
                    range(left[0], right[0] + direction, direction),
                ):
                    ocean[i, j] += 1
    return ocean


def count_crossings(ocean):
    return (ocean > 1).sum()


if __name__ == "__main__":
    # test
    ocean = setup(10)
    print(read_input("data/day5test.txt", ocean))
    print(count_crossings(ocean))
    # part 1
    ocean = setup(1000)
    read_input("data/day5input.txt", ocean, diagonals=False)
    print(count_crossings(ocean))
    # part 2
    ocean = setup(1000)
    read_input("data/day5input.txt", ocean)
    print(count_crossings(ocean))
