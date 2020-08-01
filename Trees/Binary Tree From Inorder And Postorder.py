'''
Given inorder and postorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree. 
Example :

Input : 
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

Return : 
            1
           / \
          2   3

'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, inorder, postorder):
        if inorder:
            mid = inorder.index(postorder.pop())
            root = TreeNode(inorder[mid])
            root.right = self.buildTree(inorder[mid+1:],postorder)
            root.left = self.buildTree(inorder[:mid],postorder)
            return root