'''
Given a binary tree, invert the binary tree and return it.
Look at the example for more details.

Example :
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4
'''
def invert(root):
    if root==None:return
    root.left,root.right=root.right,root.left
    invert(root.left)
    invert(root.right)
    
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        invert(A)
        return A