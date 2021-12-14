from typing import List, Tuple

def solution1(input: List[Tuple[str, str]]):
    """
    Solution to problem 1.
    """
    maxx =max([coords[0] for coords in input[0]])
    maxy = max([coords[1] for coords in input[0]])
    grid = [[False for _ in range(maxx+1)] for _ in range(maxy+1)]
    for point in input[0]:
        grid[point[1]][point[0]] = True
    axis, count = input[1][0]
    if axis == 'x':
        for i in range(maxy+1):
            for j in range(count, maxx+1):
                grid[i][count-(j-count)] = grid[i][j] or grid[i][count-(j-count)]
                grid[i][j] = False
    else:
        for i in range(count, maxy+1):
            for j in range(maxx+1):
                grid[count-(i-count)][j] = grid[i][j] or grid[count-(i-count)][j]
                grid[i][j] = False
    return sum([sum(row) for row in grid])

    

def solution2(input: List[List[int]]):
    """
    Solution to problem 2.
    """
    maxx =max([coords[0] for coords in input[0]])
    maxy = max([coords[1] for coords in input[0]])
    grid = [[False for _ in range(maxx+1)] for _ in range(maxy+1)]
    for point in input[0]:
        grid[point[1]][point[0]] = True
    for fold in input[1]:
        axis, count = fold
        if axis == 'x':
            for i in range(maxy+1):
                for j in range(count, maxx+1):
                    grid[i][count-(j-count)] = grid[i][j] or grid[i][count-(j-count)]
                    grid[i][j] = False
        else:
            for i in range(count, maxy+1):
                for j in range(maxx+1):
                    grid[count-(i-count)][j] = grid[i][j] or grid[count-(i-count)][j]
                    grid[i][j] = False
    for row in grid:
        if sum(row) > 1:
            for i, char in enumerate(row):
                if char:
                    print('#', end='')
                else:
                    print(' ', end='')
                if sum(row[i+1:]) == 0:
                    print()
                    break

    return sum([sum(row) for row in grid])


if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[Tuple[Tuple[int, int], Tuple[str, int]]] = [[x for x in f.split("\n")] for f in f.read().split('\n\n')]
        input[0] = [[int(y) for y in x.split(",")] for x in input[0]]
        input[1] = [[i for i in x.split(" ")[-1].split("=")] for x in input[1]]
        input[1] = [[x[0], int(x[1])] for x in input[1]]
    print(solution1(input))
    print(solution2(input))