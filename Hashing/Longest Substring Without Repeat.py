'''
Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        i = j = result = 0
        sz = len(A)
        storage = set()

        while i < sz and j < sz:
            if A[j] in storage:
                storage.remove(A[i])
                i += 1
            else:
                storage.add(A[j])
                j += 1
                result = max(result, j-i)

        return (result)