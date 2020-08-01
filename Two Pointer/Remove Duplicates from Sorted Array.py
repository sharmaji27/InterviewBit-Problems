'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example:
Given input array A = [1,1,2],
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        p = 1

        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                A[p]=A[i]
                p+=1
        
        return p