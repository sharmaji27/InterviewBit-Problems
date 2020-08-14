'''
Given A and B you have to find all stepping numbers in range A to B.

The stepping number:

A number is called as a stepping number if the adjacent digits have a difference of 1.

e.g. 123 is stepping number, but 358 is not a stepping number



Input Format
First argument is an integer A.

Second argument is an integer B.



Output Format
Return a integer array sorted in ascending order denoting the stepping numbers between A and B.



Example Input
Input 1:

 A = 10
 B = 20


Example Output
Output 1:

 [10, 12]


Example Explanation
Explanation 1:

 All stepping numbers are 10 , 12 

'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        h  = [0,1,2,3,4,5,6,7,8,9]
        for i in h:
            last_ele  = int(str(i)[-1])
            if last_ele<9:
                first_no  = int(str(i)+str(last_ele+1))
                if first_no<=B:
                    h.append(first_no)
            if last_ele>0:
                second_no = int(str(i)+str(last_ele-1))
                if second_no<=B:
                    h.append(second_no)
            if h[-1]>=B:
                break
        
        h = list(set(h))
        h.sort()
        res = []
        for i in h:
            if A<=i<=B:
                res.append(i)
        return res