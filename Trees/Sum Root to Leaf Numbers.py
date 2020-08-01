'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
'''
def dfs(root,ans,path):
    if root==None:
        return
    
    path = path+str(root.val)
    if root.left==None and root.right==None:
        ans.append(int(path))
    dfs(root.left,ans,path)
    dfs(root.right,ans,path)
    
    
class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        ans = []
        path=''
        dfs(A,ans,path)
        return sum(ans)%1003