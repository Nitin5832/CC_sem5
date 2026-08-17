class Solution(object):
    def maxProduct(self, nums):
        best=nums[0]
        worst=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            prev=best
            best=max(nums[i]*best,max(nums[i]*worst,nums[i]))
            worst=min(nums[i]*prev,min(nums[i]*worst,nums[i]))
            ans=max(best,ans)
        return ans

        