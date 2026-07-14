class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            if len(nums)==len(set(nums)):
                return False
            return True