'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
 NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. 
 Do not print the output, instead return values as specified. Still have a doubt? Checkout Sample Codes for more details. 
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, a):
        n = len(a)
        ap = [a[i] + i for i in range(n)]
        am = [a[i] - i for i in range(n)]
        return max(max(ap) - min(ap), max(am) - min(am))