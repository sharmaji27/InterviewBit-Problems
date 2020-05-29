'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, n):
        t1 = head
        t2 = head
        
        for _ in range(n):
            if t2:
                t2 = t2.next
            else:
                return head.next
        if t2 == None:
            return head.next
        while t2.next:
            t1 = t1.next
            t2 = t2.next
        t1.next = t1.next.next
        return head