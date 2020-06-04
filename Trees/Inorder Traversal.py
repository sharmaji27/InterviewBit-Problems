'''
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,3,2].

Using recursion is not allowed.
'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, root):
        stack = []
        l = []
        curr = root
        
        while 1:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                l.append(curr.val)
                curr = curr.right
            else:
                break
        return l
        