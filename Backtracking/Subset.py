'''
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
'''
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        res = []
        A.sort(reverse=True)
        
        for i in range(len(A)):
            x = [A[i]]
            n = [x+y for y in res]
            res+=n
            res+=[x]
            print(res)
        
        res.append([])
        res.reverse()
        return res