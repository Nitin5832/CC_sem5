class Solution(object):
    def largestRectangleArea(self, heights):
        Max = 0
        left=[]
        right=[]
        st=[]
        for i in range (len(heights)):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if not st:
                left.append(-1)
            else:
                left.append(st[-1])
            st.append(i)

        while st :
            st.pop()

        for i in range (len(heights)-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if not st:
                right.append(len(heights))
            else:
                right.append(st[-1])
            st.append(i)
    

        for i in range(1,len(heights)+1):
            area=heights[i-1]*(right[-i]-left[i-1]-1)    
            Max=max(area,Max)
    
        return Max
            


        