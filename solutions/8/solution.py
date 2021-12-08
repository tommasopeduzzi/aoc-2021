from typing import List
import collections

def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())

def solution1(notes: List[List[str]]):
    """
    Solution to problem 1.
    """
    result: int = 0
    for row in notes:
        number: str = ''
        for output in row[1]:
            if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
                result += 1
    return result
                 

def solution2(notes: List[List[str]]):
    """
    Solution to problem 2.
    """
    result: List[int] = []
    for cnt, row in enumerate(notes):
        row[0].sort(key=len)
        print(row[0])
        row[0].remove('')
        inputbylength = {}
        for i in row[0]:
            if len(i) not in inputbylength.keys():
                inputbylength[len(i)] = []
            inputbylength[len(i)].append(i)
        
        digit = {}
        string = {}
        digit[inputbylength[2][0]] = '1'
        string[1] = inputbylength[2][0]
        digit[inputbylength[4][0]] = '4'
        string[4] = inputbylength[4][0]
        digit[inputbylength[7][0]] = '8'
        string[8] = inputbylength[7][0]
        digit[inputbylength[3][0]] = '7'
        string[7] = inputbylength[3][0]
        for i in inputbylength[6]:
            if set(string[4]).issubset(set(i)):
                digit[i] = '9'
                string[9] = i
            elif set(string[7]).issubset(set(i)) and not set(string[4]).issubset(set(i)):
                digit[i] = '0'
                string[0] = i
            else:
                digit[i] = '6'
                string[6] = i
        for i in inputbylength[5]:
            if set(string[1]).issubset(set(i)):
                digit[i] = '3'
                string[3] = i
            elif set(i).issubset(set(string[6])):
                digit[i] = '5'
                string[5] = i
            else:
                digit[i] = '2'
                string[2] = i
        number: str = ''
        row[1].remove('')
        print(row[1])
        for output in row[1]:
            for i, stuff in enumerate(string.items()):
                if same_permutation(list(stuff[1]), list(output)):
                    number += digit[stuff[1]]
                    break
        result.append(int(number))
    return sum(result)
    


if __name__ == "__main__":
    with open('input.txt') as f:
        notes: List[int] = [[[y for y in x.split(" ")] for x in f.split('|')] for f in f.read().split('\n')]
        print(solution1(notes))
    print(solution1(notes))
    print(solution2(notes))