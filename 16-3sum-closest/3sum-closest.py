class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while (j<k):
                sum=nums[i]+nums[j]+nums[k]

                if sum==target:
                    return sum

                if (abs(ans-target)>abs(sum-target)):
                    ans=sum

                if (sum<target):
                    j+=1
                else :
                    k-=1
            
        return ans
        
        