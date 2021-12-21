import numpy as np
import heapq


def find_lows(lavatubes):
    left = np.less(lavatubes[1:-1, 1:-1], lavatubes[1:-1, 0:-2])
    right = np.less(lavatubes[1:-1, 1:-1], lavatubes[1:-1, 2:])
    up = np.less(lavatubes[1:-1, 1:-1], lavatubes[0:-2, 1:-1])
    down = np.less(lavatubes[1:-1, 1:-1], lavatubes[2:, 1:-1])
    mask = left & right & up & down
    return lavatubes[1:-1, 1:-1][mask], np.argwhere(mask)


def sum_risk(lows):
    return sum(lows) + len(lows)


def get_basin_size(co, lava, done):
    size = 1
    lco = (co[0], co[1] - 1)
    rco = (co[0], co[1] + 1)
    uco = (co[0] - 1, co[1])
    dco = (co[0] + 1, co[1])
    left = lava[lco] == 0
    right = lava[rco] == 0
    up = lava[uco] == 0
    down = lava[dco] == 0
    if not (left or right or up or down):
        return size
    else:
        done.append(co)
        if left and lco not in done:
            size += get_basin_size(lco, lava, done)
        if right and rco not in done:
            size += get_basin_size(rco, lava, done)
        if up and uco not in done:
            size += get_basin_size(uco, lava, done)
        if down and dco not in done:
            size += get_basin_size(dco, lava, done)
        return size


def part2(lavatubes, locations):
    locs = [tuple(loc) for loc in locations]
    lavatubes = np.where(lavatubes >= 9, 9, 0)
    count = -1
    for loc in locs:
        lavatubes[loc] = count
        count -= 1
    lava = np.pad(lavatubes, (1, 1), constant_values=(9, 9))
    print(lava)
    basinsizes = []
    for loc in locs:
        loc = (loc[0] + 1, loc[1] + 1)
        heapq.heappush(basinsizes, get_basin_size(loc, lava, []))
    print(basinsizes)
    answer = np.prod(heapq.nlargest(3, basinsizes))
    print(answer)


if __name__ == "__main__":
    with open("data/day9input.txt") as fp:
        lavalist = []
        for line in fp:
            row = list(line.rstrip())
            lavalist.append(row)
        lavatubes = np.array(lavalist, dtype=np.int64)
        lavatubes = np.pad(lavatubes, (1, 1), constant_values=(10, 10))
        print(lavatubes)
        lows, locations = find_lows(lavatubes)
        print(sum_risk(lows))
        part2(lavatubes[1:-1, 1:-1], locations)
