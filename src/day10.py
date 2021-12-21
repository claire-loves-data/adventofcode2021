import numpy as np
import heapq

def part1():
    lefts = ["(", "[", "{", "<"]
    rights = [")", "]", "}", ">"]
    match = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    totalpoints = 0
    with open("data/day10input.txt") as fp:

        for line in fp:
            thestack = []
            for char in line:
                if char in lefts:
                    thestack.append(char)
                elif char in rights:
                    if match[thestack.pop()] == char:
                        ...
                    else:
                        totalpoints += points[char]
    print(totalpoints)

def part2():
    lefts = ["(", "[", "{", "<"]
    rights = [")", "]", "}", ">"]
    match = {"(": ")", "[": "]", "{": "}", "<": ">"}
    ac_points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    with open("data/day10input.txt") as fp:
        for line in fp:
            fail = False
            thestack = []
            for char in line:
                if char in lefts:
                    thestack.append(char)
                elif char in rights:
                    if match[thestack.pop()] != char:
                        fail = True
                        continue
            if not fail:
                print(thestack)
                complement = []
                while len(thestack) > 0:
                    complement.append(match[thestack.pop()])
                score = 0
                print(complement)
                for char in complement:
                    score = 5 * score + ac_points[char]
                heapq.heappush(scores, score)
    print(int(np.median(scores)))

if __name__ == "__main__":
    part1()
    part2()
    