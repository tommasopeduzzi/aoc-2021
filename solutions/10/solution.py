from typing import List
import collections

def solution1(input: List[List[str]]):
    """
    Solution to problem 1.
    """
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }
    cost_per_bracket = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    cost = 0
    last_char = None
    for line in input:
        expected = []
        for char in line:
            if char in brackets.keys():
                expected.append(brackets[char])
            elif char in brackets.values():
                if char != expected.pop():
                    cost += cost_per_bracket[char]
                    break
            last_char = char

    return cost
    
def solution2(brackets: List[List[str]]):
    """
    Solution to problem 2.
    """
    brackets = {
        '{': '}',
        '[': ']',
        '(': ')',
        '<': '>'
    }
    cost_per_bracket = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    scores = []
    for line in input:
        expected = []
        score = 0
        incomplete = True
        for char in line:
            if char in brackets.keys():
                expected.append(brackets[char])
            elif char in brackets.values():
                if char != expected.pop():
                    incomplete = False
                    break
        if not incomplete:
            continue
        expected.reverse()
        for i in expected:
            score *= 5
            score += cost_per_bracket[i]
        scores.append(score)
    scores.sort()
    return scores[len(scores)//2]

if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[List[str]] = [list(f) for f in f.read().split('\n')]
    print(solution1(input))
    print(solution2(input))