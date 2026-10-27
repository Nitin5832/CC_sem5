class Solution(object):
    def thirdMax(self, nums):
        a=set(nums)
        b=list(a)
        b.sort()

        if len(b)>=3:
            return b[-3]
        return b[-1]

        
        