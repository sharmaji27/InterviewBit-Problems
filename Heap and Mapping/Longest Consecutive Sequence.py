'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.


'''
from heapq import heappush,heappop,heapify
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        A=list(set(A))
        
        heapify(A)
        prev = -float('inf')
        r=1
        m = 0
        i = len(A)-1
        
        while i!=-1:
            curr = heappop(A)
            if prev+1==curr:
                r+=1
            else:
                r=1
            m = max(m,r)
            prev=curr
            i-=1
        
        return (m)