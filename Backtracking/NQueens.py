'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = [['.']*A for _ in range(A)]

        def check(x,y,board):
            for i in range(A):
                for j in range(A):
                    if board[i][j]=='Q':
                        if i==x or j==y or (x-y)==(i-j) or (x+y)==(i+j):
                            return False
            return True
        
        def solve(board,qn,ans):
            if qn==A:
                to_append = [''.join(sa) for sa in board]
                ans.append(to_append)
                return
        
            for c in range(A):
                if check(qn,c,board):
                    board[qn][c] = 'Q'
                    solve(board,qn+1,ans)
                    board[qn][c] = '.'
        
        ans = list()
        solve(board,0,ans)
        return ans