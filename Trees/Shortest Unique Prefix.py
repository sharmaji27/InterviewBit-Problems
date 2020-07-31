'''
Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
 NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
'''
from collections import defaultdict
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        prefixes = defaultdict(int)
        for word in A:
            for i in range(len(word)):
                prefixes[word[:i]]+=1
        
        out = []
        
        for word in A:
            res = word
            for i in range(len(word)):
                pre = word[:i]
                if prefixes[pre]==1:
                    res = pre
                    break
            out.append(res)
        return out