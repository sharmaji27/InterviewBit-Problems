'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
'''
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, arr):
        n = len(arr)
        for i in range(0, n): 
            arr[i] += (arr[arr[i]] % n) * n 
        for i in range(0, n): 
            arr[i] = int(arr[i] / n) 
        return arr