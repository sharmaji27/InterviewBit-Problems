'''
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level order traversal of the tree when depth of the tree is much greater than number of nodes on a level.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        q = [A]
        res = []
        while q:
            tempq = []
            level = []
            while q:
                curr = q.pop(0)
                level.append(curr.val)
                if curr.left:tempq.append(curr.left)
                if curr.right:tempq.append(curr.right)
            q = tempq
            res.append(level)
        return res