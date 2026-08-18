class Solution(object):
    def maxSubarraySumCircular(self, nums):
        best=curr_max=nums[0]
        worst=curr_worst=nums[0]
        total=nums[0]
        
        for x in nums[1:]:
            total+=x
            curr_max=max(x,curr_max+x)
            best=max(best,curr_max)

            curr_worst=min(x,curr_worst+x)
            worst=min(worst,curr_worst)

        if best<0:
            return best
        return max(best,total-worst)
