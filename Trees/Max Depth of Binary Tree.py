'''
Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node. 
Example :

         1
        /
       2
max depth = 2.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
mx = 0
def find_max(root,level):
    global mx
    if root==None:return
    mx = max(mx,level)
    find_max(root.left,level+1)
    find_max(root.right,level+1)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global mx
        mx = 0
        find_max(root,1)
        return mx