class Solution(object):
    def findMaxAverage(self, nums, k):
        current=sum(nums[:k])
        best=current

        for i in range(k,len(nums)):
            current+=nums[i]
            current-=nums[i-k]
            best = max(best,current)

        return best/float(k)

        