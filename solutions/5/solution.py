from typing import List

def solution1(lines: List[List[List[int]]]):
    """
    Solution to problem 1.
    """
    board = [[0 for i in range(1000)] for i in range (1000)]
    for line in lines:
        x1, y1, x2, y2 = [i for coords in line for i in coords]
        if x1 == x2:
            ymin, ymax = min(y1, y2), max(y1, y2)
            for y in range(ymin, ymax+1):
                board[y][x1] += 1
        elif y1 == y2:
            xmin, xmax = min(x1, x2), max(x1, x2)
            for x in range(xmin, xmax+1):
                board[y1][x] += 1
    output = 0
    for row in board:
        for i in row:
            if i > 1:
                output += 1
    return output
                 

def solution2(lines: List[List[List[int]]]):
    """
    Solution to problem 2.
    """
    board = [[0 for i in range(1000)] for i in range (1000)]
    for line in lines:
        x1, y1, x2, y2 = [i for coords in line for i in coords]
        if x1 == x2:
            ymin, ymax = min(y1, y2), max(y1, y2)
            for y in range(ymin, ymax+1):
                board[y][x1] += 1
        elif y1 == y2:
            xmin, xmax = min(x1, x2), max(x1, x2)
            for x in range(xmin, xmax+1):
                board[y1][x] += 1
        else:
            if x1 > x2 and y1 > y2:
                way = [-1, -1]
            elif x1 > x2 and y1 < y2:
                way = [-1, 1]
            elif x1 < x2 and y1 > y2:
                way = [1, -1]
            else:
                way = [1, 1]
            while x1 != x2+way[0] and y1 != y2+way[1]:
                board[y1][x1] += 1
                x1 += way[0]
                y1 += way[1]
    output = 0
    for row in board:
        for i in row:
            if i > 1:
                output += 1
    return output


if __name__ == "__main__":
    with open('input.txt') as f:
        lines: List[str] = [[[int(z) for z in y.split(",")] for y in x.split("->")] for x in f.read().split("\n")]
    print(solution1(lines))
    print(solution2(lines))