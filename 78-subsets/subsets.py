class Solution(object):
    def subsets(self, nums):
        subset=[]
        ans=[]

        def allss(i):
            if i==len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[i])
            allss(i+1)

            subset.pop()
            allss(i+1)
        allss(0)
        return ans

        return ans
            
