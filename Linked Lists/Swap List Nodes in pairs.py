'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        start=ListNode(0)
        start.next=A
        A=start
        while A.next and A.next.next:
            temp=A.next.next
            A.next.next=temp.next
            temp.next=A.next
            A.next=temp
            A=A.next.next
        return start.next
            
            