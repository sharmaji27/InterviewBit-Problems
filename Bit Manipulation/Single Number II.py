'''
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer.
Constraints:

2 <= N <= 5 000 000  
0 <= A[i] <= INT_MAX
For Examples :

Example Input 1:
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Example Output 1:
    4
Explanation:
    4 occur exactly once
Example Input 2:
    A = [0, 0, 0, 1]
Example Output 2:
    1
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        
        #Complexity of this solution is O(32*N) = O(N)
        
        # Assumging 32 bit integer
        INT_SIZE = 32
        
        result = 0
        
        # Iterate for every bit position
        for i in range(0,INT_SIZE):
            
            sm = 0
            
            # Used to check if ith bit is 1 or not.
            x = (1<<i)
            
            for j in range(0,len(A)):
                
                # This will only be true, if ith bit is set (=1)
                if(A[j]&x):
                    sm = sm+1
                    
            # Set ith bit  of result based on whether the ith bit occured 3 times or not.
            # Only the bits that occured 1 time will be 1
            if (sm % 3) :
                result = result | x
                
        return result