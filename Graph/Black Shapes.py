'''
Given N x M character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
Example:

Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.

XXX
XXX
XXX
is just one single connected black shape.
'''
class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        for i in range(len(A)):
            A[i]=list(A[i])
        
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def mark_neighbours(a,b):
            q = [(a,b)]
            while q:
                i,j = q.pop(0)
                for dx,dy in dire:
                    if 0<=i+dx<rows and 0<=dy+j<cols and A[i+dx][j+dy]=='X':
                        q.append((i+dx,j+dy))
                        A[i+dx][j+dy]='XV'
        
        rows = len(A)
        cols = len(A[0])
        c = 0
        
        for i in range(rows):
            for j in range(cols):
                if A[i][j]=='X':
                    mark_neighbours(i,j)
                    c+=1
        return c