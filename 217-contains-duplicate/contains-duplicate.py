class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            if len(nums)==len(set(nums)):
                return False
            for i in range(len(nums)):
                if nums[i] in nums[(i+1):(len(nums))]:
                    return True