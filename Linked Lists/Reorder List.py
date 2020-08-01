'''
Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if head == None:
            return []
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_list = slow.next
        slow.next = None

        prev = None
        curr = second_list

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second_list = prev
        first_list = head

        while second_list:
            temp1 = first_list.next
            temp2 = second_list.next
            second_list.next = None
            first_list.next = second_list
            second_list.next = temp1
            first_list = first_list.next.next
            second_list = temp2

        return head
 