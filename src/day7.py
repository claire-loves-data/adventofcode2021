import numpy as np


def part1():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    median_pos = round(np.median(crabs))
    abs_diffs = [abs(crab - median_pos) for crab in crabs]
    print(sum(abs_diffs))
    with open("data/day7input.txt") as fp:
        crabs = [int(c) for c in fp.readline().rstrip().split(",")]
    print(sum([abs(crab - round(np.median(crabs))) for crab in crabs]))


def cost_function(distance):
    cost = distance
    for i in range(distance - 1):
        distance = distance - 1
        cost += distance
    return cost


def part2():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


if __name__ == "__main__":
    with open("data/day7input.txt") as fp:
        crabs = [int(c) for c in fp.readline().rstrip().split(",")]
    direction = 1
    pos = int(round(len(crabs) / 2))
    last_val = None
    for i in range(len(crabs) * 2):

        val = sum([cost_function(abs(crab - pos)) for crab in crabs])
        print(pos, val, direction)
        tried = [pos]
        if last_val is not None:
            if last_val < val:
                direction = direction * -1
        last_val = val
        tried.append((pos))
        pos = pos + direction
        if pos > len(crabs):
            direction = direction * -1
        while pos in tried:
            pos = pos + direction
