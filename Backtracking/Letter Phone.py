'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''
class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        phone = {'0':'0','1':'1','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz'}
        
        if A=='':return
        if len(A)==1:return phone[A]
        
        back = self.letterCombinations(A[1:])
        front = phone[A[0]]
        
        return [f+b for f in front for b in back]