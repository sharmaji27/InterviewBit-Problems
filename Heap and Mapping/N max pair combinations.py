'''
Given two arrays A & B of size N each.
Find the maximum N elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

Example:

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}

Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+6),
9    (4+5),
8    (2+6)
'''
from heapq import heapify,heappop,heappush
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        heap = []
        # heapify(heap)
        A.sort(reverse=True)
        B.sort(reverse=True)
        for a in A:
            for b in B:
                v=a+b
                if len(heap)<len(A):
                    heappush(heap,v)
                else:
                    if heap[0]<v:
                       heappop(heap)
                       heappush(heap,v)
                    else:
                        break
        heap.sort(reverse=True)
        return heap