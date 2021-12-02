aim = 0
horizontal = 0
depth = 0
    
with open("input.txt") as fp:
    for line in fp:
        val = int(line[-2])
        if "forward" in line:
            horizontal += val
            if aim != 0:
                depth += val*aim
        elif "down" in line:
            aim += val
        elif "up" in line:
            aim -= val
print(depth*horizontal)