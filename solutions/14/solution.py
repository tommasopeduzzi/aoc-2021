from types import new_class
from typing import Counter, Dict, List, Tuple
import collections

def solution1(input: Tuple[str, Dict[str, str]]):
    """
    Solution to problem 1.
    """
    polymer = list(input[0])
    for i in range(10):
        to_insert = []
        for i in range(1, len(polymer)):
            key = "".join(polymer[i-1:i+1]) 
            if key in input[1].keys():
                to_insert.append((i, input[1][key]))
        for i, c in reversed(to_insert):
            polymer.insert(i, c)
    mostcommon = collections.Counter(polymer).most_common()[0]
    leastcommon = collections.Counter(polymer).most_common()[-1]
    return mostcommon[1] - leastcommon[1]

def solution2(input: Tuple[str, Dict[str, str]]):
    """
    Solution to problem 2.
    """
    polymer, rules = input
    pairs = Counter()
    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1
    
    for i in range(40):
        new_pairs = Counter()
        for pair, count in pairs.items():
            new_pairs[pair[0] + rules[pair]] += count
            new_pairs[rules[pair] +pair[1]] += count
        pairs = new_pairs

    letters = Counter()
    for pair, count in pairs.items():
        for letter in pair: 
            letters[letter] += count
    
    letters[polymer[0]] += 1
    letters[polymer[-1]] += 1
    return max(letters.values())//2 - min(letters.values())//2

if __name__ == "__main__":
    with open('input.txt') as f:
        input: Tuple[str, Dict[str, str]] = [[x for x in f.split("\n")] for f in f.read().split('\n\n')]
        input[0] = input[0][0]
        dict = {}
        for line in input[1]:
            if line  == '': continue
            key, value = line.split(' -> ')
            dict[key] = value
        input[1] = dict
    print(solution1(input))
    print(solution2(input))