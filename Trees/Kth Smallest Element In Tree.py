'''
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
 NOTE : You may assume 1 <= k <= Total number of nodes in BST
'''
import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root,res,k):
    if root==None:return
    heapq.heappush(res,-root.val)
    if len(res)>k:heapq.heappop(res)
    inorder(root.left,res,k)
    inorder(root.right,res,k)

class Solution:
    def kthsmallest(self, root: TreeNode, k: int) -> int:
        res = []
        heapq.heapify(res)
        inorder(root,res,k)
        return -res[0]