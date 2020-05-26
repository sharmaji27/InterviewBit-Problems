'''
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        p=1
        d={A[0]:1}
        
        for i in range(1,len(A)):
            if A[i] in d:
                d[A[i]] += 1
            else:
                d[A[i]] = 1
        
            if d[A[i]]<=2:
                A[p]=A[i]
                p+=1
        
        return p