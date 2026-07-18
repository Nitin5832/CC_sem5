import math
class Solution(object):
    def findGCD(self, nums):
        a=max(nums)
        b=min(nums)
        while b != 0:
            a, b = b, a % b        
        return abs(a)