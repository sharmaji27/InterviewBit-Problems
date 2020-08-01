'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''
class Solution:
    def rotate(self, A):
        r = len(A)
        c = len(A[0])
        
        for i in range(r):
            for j in range(i,c):
                A[i][j] , A[j][i] = A[j][i] , A[i][j]
        
        for i in range(r):
            for j in range(c//2):
                A[i][j],A[i][c-j-1] = A[i][c-j-1],A[i][j]
        
        return A