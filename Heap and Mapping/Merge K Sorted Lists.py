'''
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
'''
from heapq import heappush,heapify,heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        h=[]
        heapify(h)
        for node in A:
            while node:
                heappush(h,node.val)
                node = node.next
        
        res = head = ListNode(0)
        
        while h:
            res.next=ListNode(heappop(h))
            res=res.next
        res.next=None
        return head.next