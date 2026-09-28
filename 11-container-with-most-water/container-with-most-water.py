class Solution(object):
    def maxArea(self, height):
        Max=0
        left=0
        right=len(height)-1

        while left<right:
            area=min(height[left],height[right])*(right-left)
            Max=max(area,Max)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return Max
        
    
       