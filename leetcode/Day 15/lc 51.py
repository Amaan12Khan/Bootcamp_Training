from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n for _ in range(n)]
        ans = []

        def canPut(r: int, c: int) -> bool:
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def nQueen(r: int):
            if r == n:
                ans.append(board[:])  # copy
                return

            for c in range(n):
                if canPut(r, c):
                    board[r] = board[r][:c] + 'Q' + board[r][c+1:]
                    nQueen(r + 1)
                    board[r] = board[r][:c] + '.' + board[r][c+1:]

        nQueen(0)
        return ans