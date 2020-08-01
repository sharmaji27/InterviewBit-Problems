'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carry = 0
        head = ListNode(0)
        l3 = head

        while carry or A or B:
            val1 = A.val if A else 0
            val2 = B.val if B else 0
            x =  val1 + val2 + carry
            carry = x//10
            l3.next = ListNode(x%10)
            l3 = l3.next
            if A: A=A.next
            if B: B=B.next
        return head.next