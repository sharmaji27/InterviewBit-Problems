'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity.
'''
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.push_left(self.root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
    
    def push_left(self,curr):
        while curr:
            self.stack.append(curr)
            curr=curr.left
            
    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        self.push_left(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
