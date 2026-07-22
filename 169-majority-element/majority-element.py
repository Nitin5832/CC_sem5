class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        a=-1
        candidate=nums[0]
        while True:
            
            count=nums.count(candidate)
            a+=count 
            if count>len(nums)/2:
                return candidate
            
            candidate=nums[a]



            
            
        
        