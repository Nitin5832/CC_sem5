class Solution(object):
    def longestSubstring(self, s, k):
        mxlen=0
        mxunique=len(set(s))

        for i in range (1,mxunique+1):
            counts={}
            right=0
            left=0
            uniquecount=0
            atleastk=0

            while(right<len(s)):
                r=s[right]
                if r not in counts or counts[r]==0:
                    counts[r]=0
                    uniquecount+=1
                counts[r]+=1

                if counts[r]==k:
                    atleastk+=1
                right+=1

                while uniquecount>i:
                    l=s[left]
                    if counts[l]==k:
                        atleastk-=1
                    counts[l]-=1

                    if counts[l]==0:
                        uniquecount-=1
                    
                    left+=1

                if uniquecount==i==atleastk:
                    mxlen=max(mxlen,right-left)

        return mxlen
                    

                    

        