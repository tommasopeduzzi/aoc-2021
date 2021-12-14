from typing import List, Tuple

def solution1(input: List[Tuple[str, str]]):
    """
    Solution to problem 1.
    """
    system = {}
    for start, finish in input:
        if start not in system:
            system[start] = []
        system[start] = system[start] + [finish]
        if finish not in system:
            system[finish] = []
        system[finish] = system[finish] + [start]
    visited = set()
    solution = []
    queue = [('start', ['start'])]  
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        for node in system[current]:
            if node == 'end':
                solution += [path + [node]]
            elif node not in path or node.isupper():
                queue.append((node, path+[node]))
    return len(solution)


def solution2(input: List[List[int]]):
    """
    Solution to problem 2.
    """
    system = {}
    for start, finish in input:
        if start not in system:
            system[start] = []
        system[start] = system[start] + [finish]
        if finish not in system:
            system[finish] = []
        system[finish] = system[finish] + [start]
    visited = set()
    solution = []
    queue = [('start', ['start'])]  
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        for node in system[current]:
            if node == 'end':
                solution += [path + [node]]
            elif node == 'start':
                continue
            elif node.isupper():
                queue.append((node, path+[node]))
            else:
                if node not in path:
                    queue.append((node, path+[node]))
                elif len(set([x for x in path if x.islower() and path.count(x)> 1])) == 0:
                    queue.append((node, path+[node]))
    return len(solution)


if __name__ == "__main__":
    with open('input.txt') as f:
        input: List[Tuple[str, str]] = [ f.split("-") for f in f.read().split('\n')]
    print(solution1(input))
    print(solution2(input))