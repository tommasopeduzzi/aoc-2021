from typing import List

def flash(input: List[List[int]], row: int, col: int, flashes: int, flashed: List[List[bool]] = None):
    """
    Flash octopus at row, col
    """
    flashes += 1
    input[row][col] = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < len(input) and j >= 0 and j < len(input[i]):
                if input[i][j] > 0:
                    input[i][j] += 1
                    if input[i][j] > 9:
                        input, flashes = flash(input, i, j, flashes)
    return input, flashes

def solution1(input: List[List[int]]):
    """
    Solution to problem 1.
    """
    flashes = 0
    for i in range(100):
        input = [[x+1 for x in row] for row in input] # increase energy levels by one
        for row, j in enumerate(input):
            for col, octopus in enumerate(j):
                if octopus > 9:
                    input, flashes = flash(input, row, col, flashes)
    return flashes
    
def solution2(input: List[List[int]]):
    """
    Solution to problem 2.
    """
    flashes = 0
    step = 0
    while True:
        step += 1
        input = [[x+1 for x in row] for row in input] # increase energy levels by one
        for row, j in enumerate(input):
            for col, octopus in enumerate(j):
                if octopus > 9:
                    input, flashes = flash(input, row, col, flashes)
        if sum(sum(row) for row in input) == 0:
            return step    

if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[List[int]] = [[int(x) for x in list(f)] for f in f.read().split('\n')]
    print(solution1(input))
    print(solution2(input))