'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2) 
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        res = []
        for i in range(len(A)-2):
            j = i+1
            k = len(A)-1
        
            while j<k:
                s = A[i]+A[j]+A[k]
                if s==0:
                    if [A[i],A[j],A[k]] not in res:
                        res.append([A[i],A[j],A[k]])
                    k-=1
                    continue
                elif s<0:
                    j+=1
                else:
                    k-=1
        return(res)