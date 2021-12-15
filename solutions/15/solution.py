from types import new_class
from typing import Counter, Dict, List, Tuple
import queue

width, height = 0, 0

def solution1(input: List[List[int]]):
    """
    Solution to problem 1.
    """
    priorityqueue = queue.PriorityQueue()
    priorityqueue.put((0, (0,0)))
    visited = [[False for _ in range(len(input[0]))] for _ in range(len(input))]
    visited[0][0] = True
    while priorityqueue:
        path, (x, y) = priorityqueue.get()
        if x == len(input)-1 and y == len(input[0])-1:
            return path
        if x-1 >= 0 and not visited[y][x-1]:
            priorityqueue.put((path + input[x-1][y], (x-1, y)))
            visited[y][x-1] = True
        if x+1 < len(input) and not visited[y][x+1]:
            priorityqueue.put((path + input[x+1][y], (x+1, y)))
            visited[y][x+1] = True
        if y-1 >= 0 and not visited[y-1][x]:
            priorityqueue.put((path + input[x][y-1], (x, y-1)))
            visited[y-1][x] = True
        if y+1 < len(input[0]) and not visited[y+1][x]:
            priorityqueue.put((path + input[x][y+1], (x, y+1)))
            visited[y+1][x] = True

def get_input(x,y):
    base = input[y%height][x%height]
    addition = (x//height+ y//height)
    while (base + addition) > 9:
        addition -= 9
    return (base + addition)

def solution2(input: List[List[int]]):
    """
    Solution to problem 2.
    """
    priorityqueue = queue.PriorityQueue()
    priorityqueue.put((0, (0,0)))
    visited = [[False for _ in range(len(input[0])*5)] for _ in range(len(input*5))]
    visited[0][0] = True
    while priorityqueue:
        path, (x, y) = priorityqueue.get()
        if x == len(input)*5-1 and y == len(input[0])*5-1:
            return path
        if x-1 >= 0 and not visited[y][x-1]:
            priorityqueue.put((path + get_input(x-1, y), (x-1, y)))
            visited[y][x-1] = True
        if x+1 < len(input)*5 and not visited[y][x+1]:
            priorityqueue.put((path + get_input(x+1, y), (x+1, y)))
            visited[y][x+1] = True
        if y-1 >= 0 and not visited[y-1][x]:
            priorityqueue.put((path + get_input(x,y-1), (x, y-1)))
            visited[y-1][x] = True
        if y+1 < len(input[0])*5 and not visited[y+1][x]:
            priorityqueue.put((path + get_input(x, y+1), (x, y+1)))
            visited[y+1][x] = True
    

if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[List[int]] = [[int(x) for x in list(f)] for f in f.read().split('\n')]
    width = len(input[0])
    height = len(input)
    print(solution1(input))
    print(solution2(input))