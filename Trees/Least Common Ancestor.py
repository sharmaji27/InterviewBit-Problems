'''
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants. 
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor 
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
'''
def traversal(root,B,C,path):
    global path_b,path_c
    if root==None:return

    path += str(root.val)+' '

    if root.val==B:path_b=path
    if root.val==C:path_c=path
    
    traversal(root.left,B,C,path)
    traversal(root.right,B,C,path)
    
    
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        global path_b,path_c
        path_b = ''
        path_c = ''
        traversal(A,B,C,'')
        ans = -1
        path_b = path_b.split()
        path_c = path_c.split()
        shorter_len = min(len(path_c),len(path_b))
        
        for i in range(shorter_len):
            if path_b[i]==path_c[i]:
                ans=path_b[i]
            else:
                break
        return ans
        