'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Input Format:

The first and the only argument contains an integer, A.
Output Format:

Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:

1 <= A <= 1000
Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, n):
        res = [[0]*n for _ in range(n)]
        dir=0
        
        r=0
        c=0
        
        for i in range(n*n):
            res[r][c] = i+1
            if dir==0:
                if c==n-1 or res[r][c+1]!=0:
                    dir=1
                    r+=1
                else:
                    c+=1
            elif dir==1:
                if r==n-1 or res[r+1][c]!=0:
                    dir=2
                    c-=1
                else:
                    r+=1
            elif dir==2:
                if c<=0 or res[r][c-1]!=0:
                    dir=3
                    r-=1
                else:
                    c-=1
            elif dir==3:
                if r<=0 or res[r-1][c]!=0:
                    dir=0
                    c+=1
                else:
                    r-=1
        return(res)