def length_to_num(length):
    if length == 2:
        return 1
    elif length == 3:
        return 7
    elif length == 4:
        return 4
    elif length == 7:
        return 8


def num_to_length(num):
    return len(num_to_pos(num))


# len 2 -> 1
# len 3 -> 7
# len 4 -> 4
# len 7 -> 8
# 4 is a subset of 9
#   find 9
# 9,6,0 are len 6
# 1 is a subset of 0,9 but not 6
#   find 6 and 0
# 2,3,5 are len 5
# 1 is a subset of 3
#   find 3
# 5 is a subset of 6
#   find 5
# 2 is neither
#   find 2


def num_to_pos(num):
    if num == 0:
        return set("to", "tl", "tr", "bl", "br", "bo")
    elif num == 1:
        return set("tr", "br")
    elif num == 2:
        return set("to", "tr", "mi", "bl", "bo")
    elif num == 3:
        return set("to", "tr", "mi", "br", "bo")
    elif num == 4:
        return set("tl", "tr", "mi", "br")
    elif num == 5:
        return set("to", "tl", "mi", "br", "bo")
    elif num == 6:
        return set("to", "tl", "mi", "bl", "br", "bo")
    elif num == 7:
        return set("to", "tr", "br")
    elif num == 8:
        return set("to", "tl", "tr", "mi", "bl", "br", "bo")
    elif num == 9:
        return set("to", "tl", "tr", "mi", "br", "bo")


def hashable(charset):
    return "".join(sorted(list(charset)))


def part1():
    with open("data/day8input.txt") as fp:
        count = 0
        for line in fp:
            output = line.split("|")[1].split()
            for item in output:
                if len(item) == 2 or len(item) == 3 or len(item) == 4 or len(item) == 7:
                    count += 1
        print(count)


def check_answer(vals: dict, output: list):
    if all(hashable(item) in vals.keys() for item in output):
        return "".join([str(vals[hashable(item)]) for item in output])


def find_singletons(vals: list) -> dict:
    known_vals = {}
    for item in vals:
        if len(item) == 2:
            known_vals[1] = hashable(item)
            known_vals[hashable(item)] = 1
        elif len(item) == 3:
            known_vals[7] = hashable(item)
            known_vals[hashable(item)] = 7
        elif len(item) == 4:
            known_vals[4] = hashable(item)
            known_vals[hashable(item)] = 4
        elif len(item) == 7:
            known_vals[8] = hashable(item)
            known_vals[hashable(item)] = 8

    return known_vals


def find_9(four, vals):
    for val in vals:
        if len(val) == 6 and set(four).issubset(set(val)):
            return {hashable(val): 9, 9: hashable(val)}


def find_0_and_6(one, nine, vals):
    table = {}
    for val in vals:
        if len(val) == 6 and hashable(val) != nine:
            if set(one).issubset(set(val)):
                table[hashable(val)] = 0
                table[0] = hashable(val)
            else:
                table[hashable(val)] = 6
                table[6] = hashable(val)
            if len(table) == 4:
                return table


def find_2_and_3_and_5(one, six, vals):
    table = {}
    for val in vals:
        if len(val) == 5:
            if set(one).issubset(set(val)):
                table[hashable(val)] = 3
                table[3] = hashable(val)
            elif set(val).issubset(set(six)):
                table[hashable(val)] = 5
                table[5] = hashable(val)
            else:
                table[hashable(val)] = 2
                table[2] = hashable(val)
            if len(table) == 6:
                return table


if __name__ == "__main__":
    total = 0
    with open("data/day8input.txt") as fp:
        for line in fp:
            parts = line.rstrip().split("|")
            output = parts[1].split()
            vals = [hashable(x) for x in parts[0].split()]
            code = [hashable(y) for y in parts[1].split()]
            known_vals = find_singletons(vals)
            assert all(x in known_vals.keys() for x in [1, 4, 7, 8])
            a = check_answer(known_vals, code)
            if a:
                print(a)
                total += int(a)
                continue
            known_vals.update(find_9(known_vals[4], vals))
            assert 9 in known_vals.keys()
            a = check_answer(known_vals, code)
            if a:
                print(a)
                total += int(a)
                continue
            known_vals.update(find_0_and_6(known_vals[1], known_vals[9], vals))
            assert 0 in known_vals.keys()
            assert 6 in known_vals.keys()
            a = check_answer(known_vals, code)
            if a:
                print(a)
                total += int(a)
                continue
            known_vals.update(find_2_and_3_and_5(known_vals[1], known_vals[6], vals))
            assert all(x in known_vals.keys() for x in [2, 3, 5])
            a = check_answer(known_vals, code)
            if a:
                print(a)
                total += int(a)
                continue
    print(total)
