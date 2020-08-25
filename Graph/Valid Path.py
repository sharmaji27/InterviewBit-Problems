'''
There is a rectangle with left bottom as  (0, 0) and right up as (x, y). There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.


Input Format

1st argument given is an Integer x.
2nd argument given is an Integer y.
3rd argument given is an Integer N, number of circles.
4th argument given is an Integer R, radius of each circle.
5th argument given is an Array A of size N, where A[i] = x cordinate of ith circle
6th argument given is an Array B of size N, where B[i] = y cordinate of ith circle
Output Format

Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).
Constraints

0 <= x, y, R <= 100
1 <= N <= 1000
Center of each circle would lie within the grid
For Example

Input:
    x = 2
    y = 3
    N = 1
    R = 1
    A = [2]
    B = [3]
Output:
    NO
   
Explanation:
    There is NO valid path in this case
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self,x,y,N,R,A,B):
        def inside_circle(r,x,y,xs,ys,n):
            for i in range(n):
                if ((xs[i]-x)**2 + (ys[i]-y)**2)**0.5 <= r:
                    return True
            return False 
        
        q = [(0,0)]
        visited = set()
        visited.add((0,0))
        dire = [(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(0,1),(1,0),(1,1)]
        
        while q:
            cx,cy = q.pop(0)
            if cx==x and cy==y:return 'YES'
            for dx,dy in dire:
                if 0<=cx+dx<=x and 0<=cy+dy<=y and not inside_circle(R,cx+dx,cy+dy,A,B,N) and (cx+dx,cy+dy) not in visited:
                    q.append((cx+dx,cy+dy))
                    visited.add((cx+dx,cy+dy))
        return 'NO'
        
        