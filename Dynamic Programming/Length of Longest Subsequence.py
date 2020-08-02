'''
Given an 1D integer array A of length N, find the length of longest subsequence which is first increasing then decreasing.



Problem Constraints
0 <= N <= 3000

-107 <= A[i] <= 107



Input Format
The first and the only argument contains an integer array A.



Output Format
Return an integer representing the answer as described in the problem statement.



Example Input
Input 1:

 A = [1, 2, 1]
Input 2:

 A = [1, 11, 2, 10, 4, 5, 2, 1]


Example Output
Output 1:

 3
Output 2:

 6


Example Explanation
Explanation 1:

 [1, 2, 1] is the longest subsequence.
Explanation 2:

 [1 2 10 4 2 1] is the longest subsequence.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        if not A:
            return 0
        n = len(A)
        dp_l2r = [1]*n
        dp_r2l = [1]*n
        
        for i in range(1,n):
            for j in range(i):
                if A[j]<A[i]:
                    dp_l2r[i] = max(dp_l2r[i],dp_l2r[j]+1)
        
        A = tuple(reversed(A))
        
        for i in range(1,n):
            for j in range(i):
                if A[j]<A[i]:
                    dp_r2l[i] = max(dp_r2l[i],dp_r2l[j]+1)
        
        dp_r2l = list(reversed(dp_r2l))
        
        res = []
        for i in range(n):
            res.append(dp_r2l[i]+dp_l2r[i]-1)
        return max(res)