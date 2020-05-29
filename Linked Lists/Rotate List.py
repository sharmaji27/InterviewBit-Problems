'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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
    def rotateRight(self, head, k):
        if head == None:
            return None
        if head.next == None:
            return head
        
        size = 0
        temp = head
        while temp:
            size+=1
            temp = temp.next
        
        k = k%size
        if k==0:
            return head
        
        fast = head
        slow = head
        
        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        
        slow.next = None
        fast.next = head
        head = temp
        
        return head
        