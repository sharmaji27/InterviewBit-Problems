'''
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, head):
        l3 = ListNode(0)
        x = l3
        
        while head:
            l3 = x
            while l3.next:
                if head.val <= l3.next.val:
                    temp = l3.next
                    l3.next = ListNode(head.val)
                    l3.next.next = temp
                    break
                l3 = l3.next
            if l3.next==None:
                l3.next = ListNode(head.val)

            head = head.next
        return x.next