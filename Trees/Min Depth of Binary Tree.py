'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
min depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_min(root,level):
    global m
    if not root: return
    if root.left==None and root.right==None:m = min(m,level+1)
    find_min(root.left,level+1)
    find_min(root.right,level+1)
    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        global m
        m = 2**31-1
        if root==None:return 0
        find_min(root,0)
        return m