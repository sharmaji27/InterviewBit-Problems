'''
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.
'''
class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(needle)==0 or len(haystack)==0:
            return -1
        l = len(needle)
        for i in range(len(haystack)):
            if  haystack[i:i+l]==needle:
                return i
        return -1