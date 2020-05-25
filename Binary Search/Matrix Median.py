'''
Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.


Input Format

The first and only argument given is the integer matrix A.
Output Format

Return the overall median of the matrix A.
Constraints

1 <= N, M <= 10^5
1 <= N*M  <= 10^6
1 <= A[i] <= 10^9
N*M is odd
For Example

Input 1:
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
Output 1:
    5
Explanation 1:
    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
    Median is 5. So, we return 5.

Input 2:
    A = [   [5, 17, 100]    ]
Output 2:
    17 ``` Matrix=
'''
from bisect import bisect_right as upper_bound 

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, m):
        mi=m[0][0]
        mx=0
        
        rows = len(m)
        cols = len(m[0])
        
        for i in range(rows):
            mi = min(mi,m[i][0])
            mx = max(mx,m[i][cols-1])
        
        desired = (rows*cols + 1) // 2
        
        while (mi < mx): 
                mid = mi + (mx - mi) // 2
                p = 0
                  
                # Find count of elements smaller than mid 
                for i in range(rows): 
                     j = upper_bound(m[i], mid) 
                     p+= j 
                if p < desired: 
                    mi = mid + 1
                else: 
                    mx = mid
        
        return(mi)