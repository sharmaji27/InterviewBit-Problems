'''
Given a binary tree, return the preorder traversal of its nodes’ values.

Example :
Given binary tree

   1
    \
     2
    /
   3
return [1,2,3].

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
    def preorderTraversal(self, A):
        stack = []
        l = [A.val]
        curr = A
        while 1:
            if curr is not None:
                if curr.val!=l[-1]:
                    l.append(curr.val)
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                curr=curr.right
                if curr:
                    l.append(curr.val)
            else:
                break

        return l