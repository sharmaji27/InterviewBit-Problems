'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, k):
        mapp = {}
        for i in A:
            if mapp.get(i+k,False) == True or mapp.get(i-k,False)==True:
                return 1
            mapp[i] = True
        return 0