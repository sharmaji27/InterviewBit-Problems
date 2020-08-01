'''
Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3
return [3,2,1].

Using recursion is not allowed.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        stack = [A]
        res = []
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        return res[::-1]