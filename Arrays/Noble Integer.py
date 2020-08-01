'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
	    n = len(A)
	    for i in range(n-1):
	        if A[i] == A[i+1]:
	            continue
	        
	        if A[i] == n-i-1:
	            return 1
	    
	    if A[n-1] == 0:
	        return 1
	        
	    return -1
        