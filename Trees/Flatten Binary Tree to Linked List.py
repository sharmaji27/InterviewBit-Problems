'''
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
'''
def preorder(root,ans):
    if root==None:return
    ans.append(root.val)
    preorder(root.left,ans)
    preorder(root.right,ans)
    
class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        ans = []
        preorder(A,ans)
        r=x=TreeNode(0)
        for i in ans:
            r.right=TreeNode(i)
            r=r.right
        return x.right