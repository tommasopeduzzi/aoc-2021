from typing import List

def solution1(fish: List[int]):
    """
    Solution to problem 1.
    """
    ages = [0 for i in range(9)]
    for age in fish:
        ages[age] += 1
    
    for i in range(80):
        newages = [0 for i in range(9)]
        for age, count in enumerate(ages):
            newages[age-1] += count
            if age == 0:
                newages[6] += count
        ages = newages
    return sum(ages)
                 

def solution2(fish: List[int]):
    """
    Solution to problem 2.
    """
    ages = [0 for i in range(9)]
    for age in fish:
        ages[age] += 1
    
    for i in range(256):
        newages = [0 for i in range(9)]
        for age, count in enumerate(ages):
            newages[age-1] += count
            if age == 0:
                newages[6] += count
        ages = newages
    return sum(ages)


if __name__ == "__main__":
    with open('input.txt') as f:
        fish: List[int] = [int(x) for x in f.read().split(',')]
    print(solution1(fish))
    print(solution2(fish))