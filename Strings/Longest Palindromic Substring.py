'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''
class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, string):
        maxLength = 1
        start = 0
        length = len(string) 
        low = 0
        high = 0

        for i in range(1, length): 
            low = i - 1
            high = i 
            while low >= 0 and high < length and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1
    
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]: 
                if high - low + 1 > maxLength: 
                    start = low 
                    maxLength = high - low + 1
                low -= 1
                high += 1
      
        return (string[start:start + maxLength]) 