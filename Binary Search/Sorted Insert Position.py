'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.

[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        f = 0
        l = 0
        r = len(A)-1
        ans = 0
        
        if B<=A[0]:
            return(0) 
        
        while l<=r:
            m = l+(r-l)//2
        
            if A[m]<=B:
                if A[m]==B:
                    f=1
                ans = m
                l = m+1
            else:
                r = m-1
        
        if f==0:
            ans+=1
        return(ans)