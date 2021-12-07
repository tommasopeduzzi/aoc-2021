from typing import List

def solution1(crabs: List[int]):
    """
    Solution to problem 1.
    """
    crabs.sort()
    minpos = crabs[len(crabs)//2]
    result = 0
    for crab in crabs:
        result += abs(crab - minpos)
    return result
                 

def solution2(crabs: List[int]):
    """
    Solution to problem 2.
    """
    crabs.sort()
    minpos = int(round(sum(crabs)/len(crabs)))
    print(minpos)
    result = 10000000000
    for pos in range(crabs[0], crabs[-1]+1):
        fuel = 0
        for crab in crabs:
            fuel += sum([i for i in range(1, abs(crab - pos) + 1)])
        result = min(result, fuel)
        print(f"{pos}: {result}")
    return result
    


if __name__ == "__main__":
    with open('input.txt') as f:
        crabs: List[int] = [int(x) for x in f.read().split(',')]
    print(solution1(crabs))
    print(solution2(crabs))