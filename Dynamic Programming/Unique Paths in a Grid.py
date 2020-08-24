'''
Given a grid of size m * n, lets assume you are starting at (1,1) and your goal is to reach (m,n). At any instance, if you are on (x,y), you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example :
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

 Note: m and n will be at most 100. 
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        rows = len(A)
        cols = len(A[0])
        if A[0][0]==1:return 0
        
        q = [(0,0)]
        c = 0
        
        while q:
            x,y = q.pop(0)
            if x==rows-1 and y==cols-1:
                c+=1
            if 0<=x+1<rows and A[x+1][y]==0:
                q.append((x+1,y))
            if 0<=y+1<cols and A[x][y+1]==0:
                q.append((x,y+1))
        return c