class Solution(object):
    def maxSubArray(self, nums):
        bestval=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            bestval=max(nums[i]+bestval,nums[i])
            ans=max(ans,bestval)

        return ans
        