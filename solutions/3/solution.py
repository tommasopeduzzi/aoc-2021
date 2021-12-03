from typing import List


def solution1(input: List[str]):
    """
    Solution to problem 1.
    """
    gamma: str = ''
    epsilon: int = ''
    
    for i in range(len(input[0])):
        currentbit: int = 0
        for j in input:
            currentbit += int(j[i])
        if currentbit > len(input)//2:
            gamma += '1'
            epsilon += '0' 
        else:
            epsilon += '1'
            gamma += '0'
    print(gamma)
    return int(gamma,2) * int(epsilon,2)

def solution2(input: List[str]):
    """
    Solution to problem 1. 
    """
    gamma: str = ''
    gamma: List[str] = input
    bit: int = 0
    while len(gamma)>1:
        ones: int = 0
        zeros: int = 0
        for i in gamma:
            if i[bit] == '1':
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            gamma = [i for i in gamma if i[bit] == '1']
        else:
            gamma = [i for i in gamma if i[bit] == '0']
        bit += 1
    print(gamma[0])
    bit = 0
    epsilon: List[str] = input
    while len(epsilon)>1:
        ones: int = 0
        zeros: int = 0
        for i in epsilon:
            if i[bit] == '1':
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            epsilon = [i for i in epsilon if i[bit] == '1']
        else:
            epsilon = [i for i in epsilon if i[bit] == '0']
        bit += 1
    print(epsilon[0])
    return int(gamma[0],2) * int(epsilon[0],2)

if __name__ == "__main__":
    with open('input.txt') as f:
        heights: List[str] = [x  for x in f.read().splitlines()]
    print(solution1(heights))
    print(solution2(heights))
