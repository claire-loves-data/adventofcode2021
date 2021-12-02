x = 0
y = 0
    
with open("input.txt") as fp:
    for line in fp:
        if "forward" in line:
            x += int(line[-2])
        elif "down" in line:
            y += int(line[-2])
        elif "up" in line:
            y -= int(line[-2])
print(x*y)