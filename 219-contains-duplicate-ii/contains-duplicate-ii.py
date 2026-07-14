class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s=set()
        for i in range (len(nums)):
            if i>k:
                s.remove(nums[i-1-k])
            
            if nums[i] in s:
                return True
            s.add(nums[i])
        
        return False
        
        