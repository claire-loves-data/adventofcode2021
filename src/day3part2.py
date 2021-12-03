def read_file():
    nums = []
    with open("data/day3input.txt") as fp:
        for line in fp:
            nums.append(int(line, 2))
    return nums


def get_bit_value(value, bit_index):
    return value >> bit_index & 1


def get_most_common_value(bit, nums):
    count1s = 0
    count = 0
    for n in nums:
        count += 1
        count1s += n >> bit & 1
    if count1s == (count / 2):
        return None
    else:
        return int(count1s > (count / 2))


def get_least_common_value(bit, nums):
    count1s = 0
    count = 0
    for n in nums:
        count += 1
        count1s += n >> bit & 1
    if count1s == (count / 2):
        return None
    else:
        return count1s < (count / 2)


def filter_and_find(bits, nums, keep=1):
    if len(bits) == 0:
        return nums
    if keep == 1:
        mcv = get_most_common_value(bits[0], nums)
    else:
        mcv = get_least_common_value(bits[0], nums)
    if mcv is None:
        mcv = keep
    remaining = []
    for num in nums:
        numbit = get_bit_value(num, bits[0])
        if mcv == numbit:
            remaining.append(num)

    if len(remaining) == 1:
        return remaining[0]
    else:
        print(len(remaining))
        return filter_and_find(bits[1:], remaining, keep=keep)


if __name__ == "__main__":
    nums = read_file()
    print(len(nums))
    o2 = filter_and_find(range(11, -1, -1), nums)
    co2 = filter_and_find(range(11, -1, -1), nums, keep=0)
    print(f"O2 = {o2}")
    print(f"CO2 = {co2}")
    print(f"answer: {o2*co2}")
