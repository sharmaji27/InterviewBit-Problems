'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

    1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric.
But the following is not:

    1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def lr_check(L,R):
    if not L and not R : return 1
    if not L or not R : return 0
    
    if L.val!=R.val:return 0

    a = lr_check(L.left,R.right)
    b = lr_check(L.right,R.left)
    return a and b

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root : return 1
        return lr_check(root.left,root.right)