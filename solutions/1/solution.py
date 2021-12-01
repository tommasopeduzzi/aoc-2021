from typing import List


def solution1(heights: List[int]):
    """
    Solution to problem 1. O(N) time & memory complexity.
    """
    solution: int = 0
    for i, height in enumerate(heights):
        if i == 0:
            continue
        if height > heights[i - 1]:
            solution += 1
    return solution

def solution2(heights: List[int]):
    """
    Solution to problem 2. O(N) time & memory complexity.
    """
    solution: int = 0
    for i in range(1, len(heights)-2):
        if (heights[i]+heights[i+1]+ heights[i+2]) > (heights[i-1] +  heights[i] + heights[i+1]):
            solution += 1
    return solution

if __name__ == "__main__":
    with open('input.txt') as f:
        heights: List[int] = [int(x) for x in f.read().split()]
    print(solution1(heights))
    print(solution2(heights))