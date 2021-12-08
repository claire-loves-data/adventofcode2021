import numpy as np


def see_sea(sea):
    baby_sharks = 0
    for i, fish in enumerate(sea):
        if fish == 0:
            sea[i] = 6
            baby_sharks += 1
        else:
            sea[i] -= 1
    sea.extend([8] * baby_sharks)
    return sea


def create_sea(fish):
    for f in fish:
        sea[f] += 1
    return sea


def update(sea):
    nextsea = sea[1:]
    nextsea.append(sea[0])
    nextsea[6] += sea[0]
    return nextsea


if __name__ == "__main__":
    fish = [3, 4, 3, 1, 2]
    for i in range(18):
        fish = see_sea(fish)
    print(len(fish))
    with open("data/day6input.txt") as fp:
        fish = [int(f) for f in fp.readline().rstrip().split(",")]
    sea = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sea = create_sea(fish)
    for i in range(256):
        sea = update(sea)
        print(sum(sea))
