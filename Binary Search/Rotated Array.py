'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        l = 0
        r = len(A)-1
        
        while l<r:
            m = l+(r-l)//2
            if A[m]>A[r]:
                l = m+1
            else:
                r = m
        
        return(A[l])