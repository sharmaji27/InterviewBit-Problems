'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
'''
def generateIPs(A, idx, curr_ip, ips):
    n = len(A)
    
    #If we have four numbers in the array, we have the base condition
    if len(curr_ip) == 4:
        # When idx is n, this means we are at the end of string
        # This means the IP is valid
        if idx == n:
            ips.append('.'.join(curr_ip))
        # If we haven't reached the end, it is invalid
        else:
            return
        
    # We run iterate over idx, idx+1, idx+2
    for i in range(idx, min(n, idx+3)):
        
        # Substring starting at idx of length 1, 2, 3
        num = int(A[idx:i+1])

        if num < 256:
            
            # Normal backtracking code when number is valid
            
            curr_ip.append(A[idx:i+1])
            generateIPs(A, i+1, curr_ip, ips)
            curr_ip.pop()
        
        # If the number was 0, this means we cannot add more in this number
        if num == 0:
            break

class Solution:

    def restoreIpAddresses(self, A):
        ips = []
        curr_ip = []
        generateIPs(A, 0, curr_ip, ips)
        return ips
        