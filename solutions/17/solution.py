from types import new_class
from typing import Counter, Dict, List, Tuple
import queue

def hits_target(target, v_x, v_y):
    min_x, min_y, max_x, max_y = target
    x,y = 0,0
    while x<= max_x and y >= min_y:
        if x>= min_x and y>= min_y and x<= max_x and y<= max_y:
            return True
        x += v_x
        y += v_y
        if not v_x == 0:
            v_x -= 1 
        v_y -= 1
    return False

def solution1(input: List[int]):
    """
    Solution to problem 1.
    """
    x_min = min(input[0][1], input[0][0])
    y_min = min(input[1][1], input[1][0])
    x_max = max(input[0][1], input[0][0])
    y_max = max(input[1][1], input[1][0])
    maxy_vel = abs(y_min) -1
    return (maxy_vel*(maxy_vel+1))/2
    

def solution2(input: List[int]):
    """
    Solution to problem 2.
    """
    x_min = min(input[0][1], input[0][0])
    y_min = min(input[1][1], input[1][0])
    x_max = max(input[0][1], input[0][0])
    y_max = max(input[1][1], input[1][0])
    result = []
    for x_vel in range(0, abs(x_max)+1):
        for y_vel in range(-abs(y_min), abs(y_min)+1):
            if hits_target((x_min, y_min, x_max, y_max), x_vel, y_vel):
                result.append((x_vel, y_vel))
    return len(result)

if __name__ == "__main__":
    with open('input.txt') as f:
        input: Tuple[Tuple[int]] = [[int(coord) for coord in coordspair.split("=")[1].split("..")] for coordspair in f.read().split(": ")[1].split(", ") ]
    print(solution1(input))
    print(solution2(input))