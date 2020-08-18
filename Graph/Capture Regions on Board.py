'''
Given a 2D character matrix A of size N x M, containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Problem Constraints
1 <= N, M <= 103



Input Format
First and only argument 2D character matrix A of size N X M.



Output Format
Make changes to the the input only as matrix is passed by reference.



Example Input
Input 1:

 A = [  [X, X, X, X],
        [X, O, O, X],
        [X, X, O, X],
        [X, O, X, X]
     ]


Example Output
Output 1:

 A = [  [X, X, X, X],
        [X, X, X, X],
        [X, X, X, X],
        [X, O, X, X]
     ]


Example Explanation
Explanation 1:

 'O' in (4,2) is not surrounded by X from below.
'''
class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        for i in range(len(A)):
            A[i] = list(A[i])
        
        rows = len(A)
        cols=  len(A[0])
        
        dire = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j]=='O' and (i==0 or i==rows-1 or j==0 or j==cols-1):
                    q=[(i,j)]
                    A[i][j]='B'
                    while q:
                        x,y = q.pop()
                        for dx,dy in dire:
                            if 0<=dx+x<rows and 0<=dy+y<cols and A[dx+x][dy+y]=='O':
                                A[dx+x][dy+y]='B'
                                q.append((dx+x,dy+y))
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j]=='B':
                    A[i][j]='O'
                elif A[i][j]=='O':
                    A[i][j]='X'