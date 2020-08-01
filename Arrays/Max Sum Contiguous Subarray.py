'''
Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:

1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:

Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
 NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. 
 Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details. 
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        mx=A[0]
        curr=0
        
        for i in range(len(A)):
            curr += A[i]
            mx = max(curr,mx)
            curr = max(curr,0)
        return(mx)
        
