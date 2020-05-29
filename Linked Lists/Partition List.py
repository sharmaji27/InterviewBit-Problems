'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
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
    def partition(self, head, x):
        l1 = ListNode(0)
        y = l1
        l2 = ListNode(0)
        z = l2
        head1 = head
        while head1:
            if head1.val < x:
                l1.next = ListNode(head1.val)
                l1 = l1.next
            else:
                l2.next = ListNode(head1.val)
                l2 = l2.next
            head1 = head1.next
        l1.next = z.next
        return y.next