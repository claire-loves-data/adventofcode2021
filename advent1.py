with open("input.txt") as fp:
    countHigher = 0
    prev = None
    for line in fp:
        if prev != None and int(line) > prev:
            countHigher += 1
        prev = int(line)
print(countHigher)