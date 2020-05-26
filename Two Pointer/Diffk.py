'''
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input : 
    A : [1 3 5] 
    k : 4
 Output : YES as 5 - 1 = 4 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, k):
        l=0
        r=1
        
        while l<len(A) and r<len(A):
            if r!=l and A[r]-A[l] ==k:
                return(1)
            elif A[r]-A[l]<k:
                r+=1
            else:
                l+=1
        return(0)