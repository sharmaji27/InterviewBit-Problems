'''
Given a 2D integer array A of size M x N, you need to find a path from top left to bottom right which minimizes the sum of all numbers along its path.

NOTE: You can only move either down or right at any point in time.



Input Format
First and only argument is an 2D integer array A of size M x N.



Output Format
Return a single integer denoting the minimum sum of a path from cell (1, 1) to cell (M, N).



Example Input
Input 1:

 A = [  [1, 3, 2]
        [4, 3, 1]
        [5, 6, 1]
     ]


Example Output
Output 1:

 9


Example Explanation
Explanation 1:

 The path is 1 -> 3 -> 2 -> 1 -> 1
 So ( 1 + 3 + 2 + 1 + 1) = 8

'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        rows = len(A)
        cols = len(A[0])
        
        for i in range(1,cols):
            A[0][i] = A[0][i]+A[0][i-1]
            
        for i in range(1,rows):
            A[i][0] = A[i][0]+A[i-1][0]
        
        for i in range(1,rows):
            for j in range(1,cols):
                A[i][j] = min(A[i][j]+A[i-1][j],A[i][j]+A[i][j-1])
        
        return A[-1][-1]