'''
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        ans = []
        stack = [[A,[A.val]]]
        
        while stack:
            curr,path = stack.pop()
            if curr.left:
                stack.append([curr.left,path+[curr.left.val]])
            if curr.right:
                stack.append([curr.right,path+[curr.right.val]])
            if sum(path)==B and curr.left==None and curr.right==None:
                ans.append(path)
            
        return ans