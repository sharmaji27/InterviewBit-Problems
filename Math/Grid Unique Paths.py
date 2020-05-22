'''
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        res = [[0]*B for _ in range(A)]

        for j in range(A):
            res[j][0] =1 
        for i in range(B):
            res[0][i]=1
        
        for i in range(1,A):
            for j in range(1,B):
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return (res[-1][-1])