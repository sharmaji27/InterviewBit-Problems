'''
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
'''
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        l = 0
        r = len(A)-1
        scan = 0
        
        while scan<=r:
            if A[scan]==0:
                A[scan],A[l] = A[l],A[scan]
                l+=1
                scan+=1
            elif A[scan]==2:
                A[scan],A[r] = A[r],A[scan]
                r-=1
            else:
                scan+=1
        return(A)