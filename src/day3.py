import numpy as np

counts1 = np.zeros(12)
n = 0
gamma = 0
epsilon = 0
with open("data/day3input.txt") as fp:
    for line in fp:
        n += 1
        num = int(line, 2)
        for i in range(11, -1, -1):
            counts1[11 - i] += num >> i & 1
gamma = sum(v << i for i, v in enumerate([c > (n / 2) for c in counts1][::-1]))
epsilon = sum(v << i for i, v in enumerate([c < (n / 2) for c in counts1][::-1]))
print(gamma, epsilon)
