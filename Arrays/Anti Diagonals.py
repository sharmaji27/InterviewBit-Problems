'''
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]
'''
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        rows = len(A)
        cols = len(A[0])
        res= []
        
        for c in range(cols):
            r=0
            re=[A[r][c]]
            while c-1>=0:
                re.append(A[r+1][c-1])
                r+=1
                c-=1
            res.append(re)
            
        for r in range(1,rows):
            c=cols-1
            re=[A[r][c]]
            while r<rows-1:
                re.append(A[r+1][c-1])
                r+=1
                c-=1
            res.append(re)
        return (res)