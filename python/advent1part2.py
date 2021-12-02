with open("input.txt") as fp:
    last_three = []
    count_higher_sum = 0
    for line in fp:
        if len(last_three) < 3:
            last_three.append(int(line))
        else:
            if sum(last_three) < sum(last_three[1:],int(line)):
                count_higher_sum += 1
            last_three.pop(0)
            last_three.append(int(line))
print(count_higher_sum)