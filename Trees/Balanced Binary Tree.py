'''
Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def height(root):
    global isBal
    if not root: return 0
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh-rh)>1:isBal= 0
    return 1+max(lh,rh)
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        global isBal
        isBal = 1
        height(root)
        return isBal