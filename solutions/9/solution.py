from typing import List
import collections

def solution1(heights: List[List[int]]):
    """
    Solution to problem 1.
    """
    solution: int = 0
    for i in range(1, len(heights)-1):
        for j in range(1, len(heights[0])-1):
            if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i][j-1]:
                solution += heights[i][j] + 1
    return solution
    

def solution2(heights: List[List[int]]):
    """
    Solution to problem 2.
    """
    solution: List[int] = []
    visited: List[tuple] = []
    for i in range(1, len(heights)-1):
        for j in range(1, len(heights[0])-1):
            if (j, i) in visited:
                continue
            if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j+1] and heights[i][j] < heights[i][j-1]:
                size:int = 0
                queue:List[tuple]= [(j, i)]
                while not len(queue) == 0:
                    x, y = queue.pop()
                    if (x, y) in visited:
                        continue
                    if heights[y-1][x]>heights[y][x] and heights[y-1][x] < 9:
                        queue.append((x, y-1))
                    if heights[y+1][x] > heights[y][x] and heights[y+1][x] < 9:
                        queue.append((x, y+1))
                    if heights[y][x-1] > heights[y][x] and heights[y][x-1] < 9:
                        queue.append((x-1, y))
                    if heights[y][x+1] > heights[y][x] and heights[y][x+1] < 9:
                        queue.append((x+1, y))
                    size += 1
                    visited.append((x, y))
                solution.append(size)
    solution.sort()
    return solution[-1] * solution[-2] * solution[-3]
    


if __name__ == "__main__":
    with open('input.txt') as f:
        heights: List[int] = [[9]+[int(x) for x in list(f)]+[9]for f in f.read().split('\n')]
    heights.pop()
    heights = [[9 for i in range(len(heights[0]))]] + heights + [[9 for i in range(len(heights[0]))]]
    print(solution1(heights))
    print(solution2(heights))