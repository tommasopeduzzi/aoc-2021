
from typing import List

class BoardField:
    """
    Represents a field on a board.
    """
    def __init__(self, number: int):
        self.number = number
        self.marked = False

def solution1(input: List[int], boards: List[List[BoardField]]):
    """
    Solution to problem 1.
    """
    for mark in input:
        for board in boards:
            for i, row in enumerate(board):
                for j, field in enumerate(row):
                    if field.number == mark:
                        field.marked = True
                    winner1: bool = True
                    winner2: bool = True
                    for check in range(5):
                        winner1 = not (not board[i][check].marked or not winner1)
                        winner2 =not( not board[check][j].marked or not winner2)
                    if winner1 or winner2:
                        return calculateoutput(board, mark)



def calculateoutput(board: List[List[BoardField]], finalNumber: int):
    """
    Calculates the output of a winning board.
    """
    output = []
    for row in board:
        for field in row:
            if not field.marked:
                output.append(field.number)
    return sum(output) * finalNumber                 

def solution2(input: List[int], boards: List[List[int]]):
    """
    Solution to problem 2.
    """
    winners: List[int] = [False] * len(boards)
    for mark in input:
        for currentboard,board in enumerate(boards):
            for i, row in enumerate(board):
                for j, field in enumerate(row):
                    if field.number == mark:
                        field.marked = True
                    winner1: bool = True
                    winner2: bool = True
                    for check in range(5):
                        winner1 = not (not board[i][check].marked or not winner1)
                        winner2 =not( not board[check][j].marked or not winner2)
                    if winner1 or winner2:
                        winners[currentboard] = True
                        if len([x for x in winners if x]) == len(boards):
                            return calculateoutput(board, mark)

if __name__ == "__main__":
    with open('input.txt') as f:
        file: List[str] = [x  for x in f.read().split("\n")]
    input: List[int] = [int(x) for x in file[0].split(",")]
    with open('input.txt') as f:    
        boards: List[List[int]] = [x for x in f.read().split("\n\n")]
        boards.pop(0)
        boards: List[List[List[BoardField]]] = [ [ [BoardField(int(x)) for x in y.split(" ") if not x == ''] for y in z.split("\n")] for z in boards]
    print(solution1(input, boards))
    print(solution2(input, boards))
