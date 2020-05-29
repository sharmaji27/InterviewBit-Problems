'''
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        count = 0
        node = A
        while node:
            count += 1
            node = node.next
        prev = None
        curr = A
        for i in range(count // 2):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        if count % 2 == 1:
            curr = curr.next
        while curr:
            if curr.val != prev.val:
                return 0
            curr = curr.next
            prev = prev.next
        return 1
       