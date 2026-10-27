class Solution(object):
    def nextGreaterElement(self, nums1, nums2):    
        ans=[-1 for i in range (len(nums1))]

        for i in range(len(nums1)):
            j=nums2.index(nums1[i])
             
            while(j<len(nums2)):
                if nums2[j]>nums1[i]:
                    ans[i]=nums2[j]
                    break
                j+=1

        return ans
        