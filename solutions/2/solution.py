from typing import List


def solution1(heights: List[List[str]]):
    """
    Solution to problem 1. O(N) time & memory complexity.
    """
    x: int = 0
    y: int = 0
    for i, directions in enumerate(heights):
        if directions[0] == 'forward':
            x += int(directions[1])
        elif directions[0] == 'down':
            y += int(directions[1])
        elif directions[0] == 'up':
            y -= int(directions[1])
    return x*y

def solution2(heights: List[int]):
    """
    Solution to problem 1. O(N) time & memory complexity.
    """
    x: int = 0
    y: int = 0
    aim: int = 0
    for i, directions in enumerate(heights):
        if directions[0] == 'forward':
            x += int(directions[1])
            y += aim * int(directions[1])
        elif directions[0] == 'down':
            aim += int(directions[1])
        elif directions[0] == 'up':
            aim -= int(directions[1])
    return x*y

if __name__ == "__main__":
    with open('input.txt') as f:
        heights: List[List[str]] = [x.split(" ") for x in f.read().splitlines()]
    print(solution1(heights))
    print(solution2(heights))
