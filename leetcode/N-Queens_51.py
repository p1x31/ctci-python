from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # positive diagonal r+c
        negDiag = set() # negative diagonal r-c

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (row + c)  in posDiag or (row - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'
                backtrack(row + 1)
                board[row][c] = '.'
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
        backtrack(0)
        return res