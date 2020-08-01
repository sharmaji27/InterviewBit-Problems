'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, head):
        if head==None:
            return 
        elif head.next==None:
            return head
        left = head
        right = head
        while right.next!=None:
            if right.next.val!=right.val:
                left.next = right.next
                left = right.next
            right = right.next
        left.next = None        
        return head