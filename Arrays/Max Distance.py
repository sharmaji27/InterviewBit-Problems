'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = [(A[i], i) for i in range(len(A))]
        A.sort()
        Min= A[0][1]
        ans = 0
        for i in range(1, len(A)):
            Min = min(Min,A[i][1])
            ans = max(ans, A[i][1]-Min)
        return ans