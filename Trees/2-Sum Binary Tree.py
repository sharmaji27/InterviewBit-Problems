'''
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes

Your solution should run in linear time and not take memory more than O(height of T).
Assume all values in BST are distinct.
Example :

Input 1: 

T :       10
         / \
        9   20

K = 19

Return: 1

Input 2: 

T:        10
         / \
        9   20

K = 40

Return: 0
'''
def inorder(root,arr):
    if root==None:
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        arr = []
        inorder(A,arr)
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]+arr[j]<B:
                i+=1
            elif arr[i]+arr[j]>B:
                j-=1
            else:
                return 1
        return 0